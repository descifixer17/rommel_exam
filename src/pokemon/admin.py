from django.contrib import admin

from .models import Pokemon, Species

# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'level', 'trainer')

    # if level >= 18 and level <= 32:
    #     print('ivysaur')


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Species)
