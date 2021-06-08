from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
    path('games/', views.Games.as_view(), name="games")
]