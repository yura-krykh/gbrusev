from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/signup.html'



    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'



class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'user/profile.html'
    login_url = 'login'

def logout_user(request):
    logout(request)
    return redirect('login')


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

class ChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

class WorkCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateWorkForm
    # model = CustomUser
    template_name = 'city\city_new.html'
    # pk = None
    # fields = ['email', 'first_name', 'last_name', 'password', 'worker', 'is_superuser', 'post', ]
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user\\user_table.html'

    def get_queryset(self):
        return CustomUser.objects.filter(worker = False)

class WorkersListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user\workers_table.html'

    def get_queryset(self):
        workers = CustomUser.objects.filter(worker = True)
        return workers

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['email', 'first_name', 'last_name', 'password', 'worker', 'is_superuser', 'post', ]
    template_name = 'city\city_edit.html'
    login_url = 'login'

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'city\city_delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})