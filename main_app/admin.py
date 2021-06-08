from django.contrib import admin
from .models import Game, Player, Record
# Register your models here.

admin.site.register(Game)
admin.site.register(Record)
admin.site.register(Player)