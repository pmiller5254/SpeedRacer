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
from .models import Player, Game, Record
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


class PlayerDetail(DetailView):
    model = Player
    template_name = "player_details.html"

class RecordCreate(CreateView):
    model = Record
    fields = ['player', 'game', 'date', 'speed', 'description']
    template_name = "record_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RecordCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('game_details', kwargs={'pk': self.object.pk})

class Signup(View):

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            return redirect("signup")

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
