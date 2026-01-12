from django.urls import path
from . import views


app_name = 'rangoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/add_page/<slug:category_name_slug>/', views.add_page, name='add_page'),
    path('category/<slug:slug>/', views.show_category, name='show_category'),
    path('page/<slug:slug>/search/', views.search_pages, name='search_pages'),
    path('category-suggestions/', views.category_suggestions, name='category_suggestions'),
    path('page-suggestions/', views.page_suggestions, name='page_suggestions'),  # URL for the AJAX suggestions
    path('like/', views.like_category, name='like_category'),
    path('goto/', views.track_url, name='goto'),
    path('accounts/about/', views.about, name='about'),

    

    #path('accounts/register/', views.register, name='register'),
    #path('accounts/login/', views.login, name='login'),
    #path('accounts/logout/', views.logout, name='logout'),
    path('accounts/register_profile/', views.register_profile, name='register_profile'),
    path('accounts/profile/<slug:username>/', views.update_profile, name='profile'),
    path('accounts/list_profiles/', views. list_profiles, name='list_profiles'),
    path('accounts/settings/', views.form_selection, name='form_selection'),
    path('accounts/restricted/', views.restricted, name='restricted'),
    
]