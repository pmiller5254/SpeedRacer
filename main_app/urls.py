from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.Games.as_view(), name="games")
]