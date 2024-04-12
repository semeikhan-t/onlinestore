from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from catalog.utils import DataMixin
from main.forms import *


def index(request):
    return render(request, 'main/index.html')


class UserRegistration(DataMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('catalog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class UserLogin(DataMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('catalog')


def logout_user(request):
    logout(request)
    return redirect('catalog')
