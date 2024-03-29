
from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField, ManyToManyField, DateField

# import user model from built in auth
from django.contrib.auth.models import User

import time
from time import strftime

from django.db.models.fields import IntegerField

# Create your models here.


class Game(Model):

    title = CharField(max_length=150)
    release_year = CharField(max_length=20)
    genre = CharField(max_length=50)
    cover_img = CharField(max_length=500)
    

    def __str__(self):
        return self.title

class Player(Model):
    name = CharField(max_length=50)
    img = CharField(max_length=500, default="https://static.wikia.nocookie.net/mario/images/c/cd/Mario_Cap.png/revision/latest?cb=20180310022043")
    bio = TextField(max_length=500)
    games = ManyToManyField(Game)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.name

    class Meta:
        ordering = ['name']


class Record(Model):

    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="records")
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="records")
    date = DateField()
    speed = IntegerField(default=0)
    description = TextField(max_length=1000)

    def __str__(self):
        return f"On {self.date}, {self.player} cleared {self.game} in {self.speed}!"
