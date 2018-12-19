#!/usr/bin/python3.7
from django import template
from photoalbum.models import Photo, Likes, Comments

register = template.Library()


@register.filter()
def count_comments(photo):
    comments = Comments.objects.filter(photo_id=photo.id)
    return len(comments)


@register.filter()
def count_likes(photo):
    likes = Likes.objects.filter(photo_id=photo.id, like=True)
    return len(likes)


@register.filter()
def likes_id(photo):
    likes = Likes.objects.filter(photo_id=photo.id, like=True)
    list_id = likes.values_list('user_id', flat=True)
    print(list_id)
    return list_id
