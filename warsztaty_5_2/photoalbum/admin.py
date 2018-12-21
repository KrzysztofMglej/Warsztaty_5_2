from django.contrib import admin
from .models import Photo, Comments, Likes


def content_display_thirty_signs(obj):
    return str(obj.content)[0:30]


content_display_thirty_signs.short_description = 'content'


def deleted(model_admin, request, query_set):
    query_set.update(deleted=True)


deleted.short_description = "Ukryj element w widoku"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', content_display_thirty_signs, 'path', 'creation_date', 'deleted']
    list_filter = ['user', 'creation_date', 'deleted']
    actions = [deleted, ]


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'photo']
    list_filter = ['user', 'photo']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'creation_date', 'photo', 'user', content_display_thirty_signs, 'deleted']
    list_filter = ['creation_date', 'photo', 'user', 'deleted']
    actions = [deleted, ]
