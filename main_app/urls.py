from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('games/', views.Games.as_view(), name="games"),
    path('games/<int:pk>/', views.GameDetail.as_view(), name="game_details"),
    path('player/<int:pk>', views.PlayerDetail.as_view(), name="player_details"),
    path('player/<int:pk>/records/new', views.RecordCreate.as_view(), name="record_create"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login")
]