from django.db import models
from users.models import User


class Photo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.ImageField(upload_to='photos')

    def __str__(self):
        return f'{self.user} Profile'


class Comments(models.Model):
    content = models.CharField(max_length=60)
    creation_date = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.photo} >>> {self.content[0:30]}"


class Likes(models.Model):
    like = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
