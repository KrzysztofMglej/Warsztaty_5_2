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
from .views import LoginUserView, LogoutUserView, RegisterUserView, ProfileView, ChangePasswordView, \
    ConfirmDeleteUserView

urlpatterns = [
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('delete_user/<int:pk>/', ConfirmDeleteUserView.as_view(), name='delete-user'),
]
