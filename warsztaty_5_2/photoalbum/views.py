from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PhotoAddForm, CommentAddForm
from .models import Photo, Likes, Comments
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
        

class LikeView(View):

    def get(self, request, photo_id):
        existing_like = Likes.objects.filter(user_id=request.user.id, photo_id=photo_id).first()
        if existing_like:
            if existing_like.like:
                existing_like.like = False
            else:
                existing_like.like = True
            existing_like.save()
        else:
            new_like = Likes.objects.create(like=True, photo_id=photo_id, user_id=request.user.id)
        return redirect('main')


class PhotoDetailView(LoginRequiredMixin, View):
    class_form = CommentAddForm

    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, pk=photo_id, deleted=False)
        form = self.class_form()
        comments = Comments.objects.filter(photo_id=photo.id, deleted=False)
        context = {'photo': photo, 'form': form, 'comments': comments}
        return render(request, "photoalbum/photo_detail.html", context)

    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, pk=photo_id)
        form = self.class_form(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            comment = Comments(content=content, photo=photo, user=request.user)
            comment.save()
            messages.success(request, "Komentarz został dodany")
        return redirect("photo-detail", photo_id=photo_id)
