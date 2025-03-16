from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="chat"),
    path("<str:language>/", views.room, name="room"),
]
