from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

# auth imports
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# import models
from .models import Player, Game, Record, User
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.all() 
        return context

class Games(TemplateView):
    template_name = "games.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.all() 
        return context

class GameDetail(DetailView):
    model = Game
    template_name ="details.html"
    

    

@method_decorator(login_required, name='dispatch')
class PlayerDetail(DetailView):
    model = Player
    template_name = "player_details.html"

@method_decorator(login_required, name='dispatch')
class PlayerUpdate(UpdateView):
    model = Player
    fields = ['bio', 'img', 'games']
    template_name = "player_update.html"

    def get_success_url(self):
        return reverse('player_details', kwargs={ 'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class RecordCreate(CreateView):
    model = Record
    fields = ['game', 'date', 'speed', 'description']
    template_name = "record_create.html"

    def form_valid(self, form):
        form.instance.player = self.request.user.player
        return super(RecordCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('game_details', kwargs={'pk': self.object.game.pk})

@method_decorator(login_required, name='dispatch')
class RecordUpdate(UpdateView):
    model = Record
    fields = ['date', 'speed', 'description']
    template_name = "record_update.html"

    def get_success_url(self):
        return reverse('player_details', kwargs={'pk': self.object.player.pk})


@method_decorator(login_required, name='dispatch')
class RecordDelete(DeleteView):
    model = Record
    template_name = "record_delete_confirmation.html"
    
    def get_success_url(self):
        return reverse('player_details', kwargs={'pk': self.object.player.pk})

class Signup(View):

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Player.objects.create(
                user = user,
                name = request.POST["username"],
                bio = "A new Speedracer!"
            )
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class Login(View):    
    def get(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("signup")
