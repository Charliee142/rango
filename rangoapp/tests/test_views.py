from django.test import TestCase
from django.urls import reverse
from rangoapp.models import Category, Page

class IndexViewTests(TestCase):

    def setUp(self):
        # Create sample categories and pages
        self.category1 = Category.objects.create(name='Category1', views=10, likes=5)
        self.category2 = Category.objects.create(name='Category2', views=20, likes=15)
        
        self.page1 = Page.objects.create(title='Page1', category=self.category1, views=50)
        self.page2 = Page.objects.create(title='Page2', category=self.category2, views=30)
    
    def test_index_view_with_no_pages_or_categories(self):
        # Delete all categories and pages
        Category.objects.all().delete()
        Page.objects.all().delete()
        
        # Call the index view
        response = self.client.get(reverse('rangoapp:index'))
        
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that the context variables are empty
        self.assertQuerySetEqual(response.context['most_viewed_pages'], [])
        self.assertQuerySetEqual(response.context['most_viewed_categories'], [])
        self.assertQuerySetEqual(response.context['most_liked_categories'], [])
    
    def test_index_view_with_pages_and_categories(self):
        """
        The index view should return the most viewed/liked categories and pages.
        """
        # Call the index view
        response = self.client.get(reverse('rangoapp:index'))
        
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that the context contains the most viewed pages and categories
        self.assertEqual(list(response.context['most_viewed_pages']), [self.page1, self.page2])
        self.assertEqual(list(response.context['most_viewed_categories']), [self.category2, self.category1])
        self.assertEqual(list(response.context['most_liked_categories']), [self.category2, self.category1])
    
    def test_session_handling(self):
        response = self.client.get(reverse('rangoapp:index'))
        
        # Check if the test cookie is set
        self.assertTrue(self.client.session.test_cookie_worked())
        
        # Check if the 'visits' key is in the session
        self.assertIn('visits', self.client.session)

