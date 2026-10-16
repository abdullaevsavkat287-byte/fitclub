
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("trainers/", views.trainers, name="trainers"),
    path("classes/", views.classes, name="classes"),
]
