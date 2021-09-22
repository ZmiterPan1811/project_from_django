from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.db.models import Q

from .models import *
from .forms import *
from .utils import *


class AboutBelarusHome(DataMixin, ListView):
    model = AboutBelarus
    template_name = 'aboutbelarus/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        if self.request.GET.get('q'):
            return AboutBelarus.objects.filter(
                Q(title__icontains=self.request.GET.get('q')) | Q(content__icontains=self.request.GET.get('q')),
                is_published=True)
        else:
            return AboutBelarus.objects.filter(is_published=True)


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'aboutbelarus/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Контакты")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        new_form = UserSendMessage(name=name, email=email, message=message)
        new_form.save()
        return redirect('home')


class PartnersProject(AboutBelarusHome):
    paginate_by = False
    template_name = 'aboutbelarus/partners.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Наши партнеры')
        return dict(list(context.items()) + list(c_def.items()))


class AboutSite(AboutBelarusHome):
    paginate_by = False
    template_name = 'aboutbelarus/about.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О проекте')
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(LoginRequiredMixin, DataMixin, DetailView):
    model = AboutBelarus
    template_name = 'aboutbelarus/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class AboutBelarusCategory(DataMixin, ListView):
    model = AboutBelarus
    template_name = 'aboutbelarus/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return AboutBelarus.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория -' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'aboutbelarus/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'aboutbelarus/login.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена.</h1>')


def logout_user(request):
    logout(request)
    return redirect('login')
