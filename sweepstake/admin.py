from django.contrib import admin
from .models import Player, Contestant, Pick

# Register your models here.

admin.site.register(Player)
admin.site.register(Contestant)
admin.site.register(Pick)
