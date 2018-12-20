"""warsztaty_5_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import HomeView, LikeView, PhotoDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='main'),
    path('like/<int:photo_id>/', LikeView.as_view(), name='like'),
    path('photo/<int:photo_id>/', PhotoDetailView.as_view(), name='photo-detail'),

]
#TODO user photos view
# TODO klasy autoadmina i flagi