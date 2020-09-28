from django.urls import path
from  . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView


urlpatterns = [
     path('dashboard/', views.dashboard, name="dashboard"),
    path('vehicle-status/', views.vehicle_status, name="vehicle-status"), 
    # path('missing-vehicle/', views.missing_vehicle, name="missing-vehicle"),
    path('compliant/', views.compliant, name="compliant"),
    path('register/', views.register, name='register'),
    path('', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),

    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('reset-password/', auth_views.PasswordResetView.as_view(template_name='citizen/password_reset.html'), name='reset_password'),
    # path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='citizen/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='citizen/password_reset_form.html'), name='password_reset_confirm'),
    # path('reset-completed/', auth_views.PasswordResetCompleteView.as_view(template_name='citizen/password_reset_completed.html'), name='password_reset_complete'),
]
