from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('sign_up/', views.signup_view, name='signup'),
    path('login/', views.login_view ,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('organizer-dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
    path('participant-dashboard/', views.participant_dashboard, name='participant_dashboard'),
]