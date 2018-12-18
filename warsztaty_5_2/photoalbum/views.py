from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PhotoAddForm
from .models import Photo, Likes
from django.views.generic import ListView, FormView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


class HomeView(LoginRequiredMixin, View):
    class_form = PhotoAddForm

    def get(self, request):
        photos = Photo.objects.all().order_by('-creation_date')
        return render(request, "photoalbum/main.html", {'form': self.class_form, 'photos': photos})

    def post(self, request):
        photos = Photo.objects.all().order_by('-creation_date')
        button = request.POST.get('button')
        if button == 'form_btn':
            form = PhotoAddForm(request.POST, request.FILES)
            user = self.request.user
            if form.is_valid():
                content = form.cleaned_data.get('content')
                photo = form.cleaned_data.get('path')
                added_photo = Photo.objects.create(content=content, user=user, path=photo)
                added_photo.save()
                messages.success(request, 'Dodano wpis')
                return render(request, "photoalbum/main.html", {'form': self.class_form, 'photos': photos})
            return render(request, "photoalbum/main.html", {'form': form, 'photos': photos})
        else:
            existing_like = Likes.objects.filter(user_id=request.user.id)
            if existing_like:
                if button == 'like_btn':
                    existing_like[0].like = True
                else:
                    existing_like[0].like = False
            else:
                # new_like = Likes.objects.create(like=True, photo_id=photo)
                pass
            #TODO brak rozwiązania problemu lików

        return render(request, "photoalbum/main.html", {'form': self.class_form, 'photos': photos})

