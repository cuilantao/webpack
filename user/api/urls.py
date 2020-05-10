from django.urls import path
from . import views;
from .views import (
    CreateUserView,
    DestroyUserView,
    FilteringUserView
)

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('delete/<pk>', DestroyUserView.as_view()),
    path('loginattempt/', FilteringUserView.as_view())
]