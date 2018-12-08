from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PhotoAddForm
from .models import Photo
from django.views.generic import ListView, FormView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


class HomeView(View):

    def get(self, request):
        form = PhotoAddForm
        photos = Photo.objects.all()
        return render(request, "photoalbum/main.html", locals())

    def post(self, request):
        form = PhotoAddForm(request.POST, request.FILES)
        user = self.request.user
        if form.is_valid():
            content = form.cleaned_data.get('content')
            photo = form.cleaned_data.get('path')
            print(photo)
            added_photo = Photo.objects.create(content=content, user=user, path=photo)
            added_photo.save()
        return render(request, "photoalbum/main.html", locals())
