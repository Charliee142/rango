from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rangoapp.views import MyRegistrationView, CustomLogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rangoapp.urls')),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),  # Use custom view
    path('accounts/logout/', CustomLogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),  # Custom password reset form
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done1.html'), name='password_reset_done'),  # Custom confirmation after submitting reset request
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm1.html'), name='password_reset_confirm'),  # Confirm password reset
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete1.html'), name='password_reset_complete'),  # Reset complete
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change1.html'), name='password_change'),  # Use custom view
    path('accounts/', include('registration.backends.simple.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
