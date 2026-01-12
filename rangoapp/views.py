from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
import requests
from django.contrib import messages
from rangoapp.forms import *
from django import forms
import json
import datetime
from django.utils import timezone
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import LogoutView
from lockdown.decorators import lockdown


def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]
    return cat_list


"""def suggest_category(request):
    cat_list = []
    starts_with = ''
    
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    cat_list = get_category_list(8, starts_with)
    return render(request, 'rango/cats.html', {'cats': cat_list })"""


def category_suggestions(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
        categories = Category.objects.filter(name__icontains=query)
        suggestions = [category.name for category in categories]  # extract the necessary data
        return JsonResponse(suggestions, safe=False)


def page_suggestions(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
        pages  = Page.objects.filter(title__icontains=query)[:5]  # Limit results for performance
        suggestions = [page.title for page in pages]  # extract the necessary data
        return JsonResponse(suggestions, safe=False)
    

def form_selection(request):
    return render(request, 'registration/form_selection.html')

@login_required
def register_profile(request):
    user = request.user
    
    # Check if the profile already exists or create one if it doesn't
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('rangoapp:profile', user.username)  # Adjust this to your desired redirect URL
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'registration/profile_registration.html', {'form': form})


@login_required
def update_profile(request, username):
    try:
        user = get_object_or_404(User, username=username)
    except User.DoesNotExist:
        return redirect('index')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'website': userprofile.website, 'picture': userprofile.picture})
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('rangoapp:profile', user.username)
        else:
            print(form.errors)
    return render(request, 'registration/update_profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})


@login_required
def list_profiles(request):
    userprofile_list = UserProfile.objects.all()
    return render(request, 'registration/list_profiles.html', {'userprofile_list' : userprofile_list})


def track_url(request):
    page_id = None
    url = '/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']

            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass
    return redirect(url)


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        # Redirect to the desired URL after successful registration
        return 'register_profile'


class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']  # Allow both GET and POST methods


@lockdown()
def index(request):
    request.session.set_test_cookie()
    most_viewed_pages = Page.objects.order_by('-views')[:5]
    most_viewed_categories = Category.objects.order_by('-views')[:5]
    most_liked_categories = Category.objects.order_by('-likes')[:5]


    context = {
        'most_viewed_pages': most_viewed_pages,
        'most_viewed_categories': most_viewed_categories,
        'most_liked_categories': most_liked_categories,
        'visits': request.session.get('visits', 0),  # Ensure 'visits' key is included in the context
        
    }
    response= render(request, 'rango/index.html', context)
    visitor_cookie_handler(request, response)
    return response


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.order_by('-views')[:5]
    category.views += 1
    category.save()

    pages = Page.objects.filter(category=category).order_by('-views')
    query = request.GET.get('query')
    # Search results, initially set as empty
    search_results = []
    if query:
   # Search functionality - filter pages based on the query within the current category
        search_results = pages.filter(title__icontains=query) 
        
        # Combine internal and external results if applicable
        search_results = list(search_results)

    context = {
        'category': category,
        'categories': categories,
        'pages': pages,
        'search_results': search_results,
        'query': query,  # To display the search term in the template if needed
    }
    return render(request, 'rango/category.html', context)


@login_required
def like_category(request):
    category_id = request.GET.get('category_id', None)
    if category_id:
        try:
            category = Category.objects.get(id=int(category_id))
            category.likes += 1
            category.save()
            return JsonResponse({'likes': category.likes})
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def search_pages(request, slug):
    if 'query' in request.GET:
        query = request.GET['query']
        url = f"https://api.bing.microsoft.com/v7.0/search?q={query}"
        headers = {"Ocp-Apim-Subscription-Key": settings.BING_API_KEY}
        response = requests.get(url, headers=headers)
        results = response.json().get('webPages', {}).get('value', [])
    else:
        results = []

    category = get_object_or_404(Category, slug=slug)

    context = {
        'category': category,
        'results': results
    }
    return render(request, 'rango/search.html', context)


@login_required
def add_category(request):
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("rangoapp:index")
        else:
            print(form.errors)
    context={
        'form': form, 
    }
    return render(request, 'rango/add_category.html', context)


@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context)


"""@login_required
def like_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category.likes += 1
    category.save()
    return redirect('rangoapp:show_category', slug=category.slug)"""


"""def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rango/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('rangoapp:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'rango/logout.html', {})"""


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


def visitor_cookie_handler(request, response):
    # Get the number of visits to the site
    visits = int(request.session.get('visits', '1'))
    
    # Get the last visit time from the cookie
    last_visit_cookie = request.session.get('last_visit', str(datetime.datetime.now()))
    last_visit_time = datetime.datetime.strptime(last_visit_cookie[:-7], "%Y-%m-%d %H:%M:%S")
    
    # If it's been more than a day since the last visit...
    if (datetime.datetime.now() - last_visit_time).days > 0:
        visits += 1
        # Update the last visit time cookie to now
        request.session['last_visit'] = str(datetime.datetime.now())
    else:
        # Set the last visit time from the current session
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits



def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
        return val

