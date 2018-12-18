from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Photo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.ImageField(upload_to='photos/')
    content = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} Profile'

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     super().save()
    #     if not self.path_small:
    #         print(self.path_small.path)
    #         img = Image.open(self.path_small.path)
    #         if img.height > 600 or img.width > 600:
    #             output_size = (600, 600)
    #             img.thumbnail(output_size)
    #             print(self.path_small)
    #             img.save(self.path_small)
    #             # img.save(self.path.path)


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
