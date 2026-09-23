from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("task/<int:pk>/toggle/", views.toggle_task, name="toggle_task"),
    path("task/<int:pk>/delete/", views.delete_task, name="delete_task"),
]
