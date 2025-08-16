from django.shortcuts import render, redirect
from django.contrib.auth import login,logout as auth_logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from .forms import CustomRegistrationForm, LoginForm, EditProfileForm, CustomPasswordChangeForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin




User = get_user_model()



def register(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")   
    else:
        form = CustomRegistrationForm()
    
    return render(request, "users/register.html", {"form": form})



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            
            participant_group, _ = Group.objects.get_or_create(name='Participant')
            user.groups.add(participant_group)

            
            user_id = urlsafe_base64_encode(force_bytes(user.id))
            token = default_token_generator.make_token(user)
            activation_link = f"http://127.0.0.1:8000/users/activate/{user_id}/{token}/"

            send_mail(
                'Activate your account',
                f'Click here to activate: {activation_link}',
                'admin@example.com',
                [user.email],
            )
            return HttpResponse("Check your email to activate your account.")
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')

def activate_account(request, idb64, token):
    try:
        user_id = urlsafe_base64_decode(idb64).decode()
        user = User.objects.get(id=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse("Account activated! You can now login.")
    else:
        return HttpResponse("Activation link is invalid!")

def dashboard_redirect(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    elif request.user.groups.filter(name='Organizer').exists():
        return redirect('organizer_dashboard')
    else:
        return redirect('participant_dashboard')

def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')

def organizer_dashboard(request):
    return render(request, 'users/organizer_dashboard.html')

def participant_dashboard(request):
    return render(request, 'users/participant_dashboard.html')

def logout_view(request):
    
    auth_logout(request)
    return redirect('login')
   
class SignUpView(CreateView):
    model = User
    form_class = CustomRegistrationForm
    template_name = "users/signup.html"
    success_url =reverse_lazy("dashboard")
    

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)   
        return redirect("profile")

class CustomLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("sign-in")

class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = "accounts/edit_profile.html"
    success_url = reverse_lazy("profile")
    login_url = reverse_lazy("sign-in")

    def get_object(self):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("profile")

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = "registration/reset_password.html"
    email_template_name = "registration/reset_email.html"
    success_url = reverse_lazy("sign-in")

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = "registration/reset_confirm.html"
    success_url = reverse_lazy("sign-in")