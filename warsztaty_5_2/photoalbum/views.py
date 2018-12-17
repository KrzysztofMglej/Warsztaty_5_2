from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, FormView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


class HomeView(View):

    def get(self, request):
        return render(request, "photoalbum/main.html", locals())

