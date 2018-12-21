from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Photo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.ImageField(upload_to='photos/')
    content = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.content[0:30]}'


class Comments(models.Model):
    content = models.CharField(max_length=60)
    creation_date = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.photo} >>> {self.content[0:30]}"


class Likes(models.Model):
    like = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.photo}: {self.like}"
