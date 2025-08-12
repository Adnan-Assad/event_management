from django.shortcuts import render, redirect
from django.contrib.auth import login,logout as auth_logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib import messages



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

def activate_account(request, user_idb64, token):
    try:
        user_id = urlsafe_base64_decode(user_idb64).decode()
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
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')
    else:
         
        return redirect('login')