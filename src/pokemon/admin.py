from django.contrib import admin

from .models import Pokemon, Species

# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'level', 'trainer', 'evolve')
        
    def evolve(self, obj):
        if obj.level >= 18 and obj.level <= 32:
            print(obj.species.name)



admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Species)
