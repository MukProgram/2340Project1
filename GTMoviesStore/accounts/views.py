from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from cart.models import Order


def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = UserCreationForm()
        return render(request,'accounts/signup.html', {'template_data':template_data})
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request,'accounts/signup.html', {'template_data':template_data})
def login(request, user=None):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',{'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {'template_data': template_data})
        auth_login(request, user)
        return redirect('index')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')
@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html', {'template_data': template_data})

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')
