from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:banco_id>/", views.resultado, name="resultado"),
]