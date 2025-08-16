

from django.urls import path
from .views import (
    signup_view, login_view, logout_view, activate_account,
    dashboard_redirect, admin_dashboard, organizer_dashboard, participant_dashboard,
    SignUpView, CustomLoginView, CustomLogoutView, ProfileView, EditProfileView,
    ChangePasswordView, CustomPasswordResetView, CustomPasswordResetConfirmView,register
)

urlpatterns = [
    
    path('sign_up/', signup_view, name='signup'),  
    path('login/', login_view, name='login'),      
    path('logout/', logout_view, name='logout'),   
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('dashboard/', dashboard_redirect, name='dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('organizer-dashboard/', organizer_dashboard, name='organizer_dashboard'),
    path('participant-dashboard/', participant_dashboard, name='participant_dashboard'),

    path('sign-up/', SignUpView.as_view(), name='sign-up'),  
    path("register/", register, name="register"),
    path('sign-in/', CustomLoginView.as_view(), name='sign-in'),
    path('sign-out/', CustomLogoutView.as_view(), name='sign-out'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password-change'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]