from django.urls import path

from . import views

urlpatterns = [
    path("manager/", views.manager, name="admin"),
    path("worker/", views.worker, name="worker"),
]
