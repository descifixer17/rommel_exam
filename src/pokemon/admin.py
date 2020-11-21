from django.contrib import admin

from .models import Pokemon, Species

# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_species', 'level', 'trainer')
        
    def get_species(self, request):
        if request.species.name == 'bulbasaur':
            if request.level >= 18 and request.level <= 32:
                request.species.name = 'Ivysaur'
                return request.species
            elif request.level > 32:
                request.species.name = 'Venasaur'
                return request.species
            else:
                return request.species

        elif request.species.name == 'charmander':
            if request.level >= 16:
                request.species.name = 'Charmeleon'
                return request.species
            else:
                return request.species
        else:
            return request.species



    get_species.short_description = 'species'
       


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Species)
