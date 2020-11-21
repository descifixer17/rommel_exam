from django.shortcuts import render
from django.views.generic.base import TemplateView

from trainer.models import Trainer
from pokemon.models import Pokemon

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        # for pokemon in Pokemon.objects.all():
        #     trainer = pokemon.trainer
        #     species = pokemon.species
        #     print(species)
        

        context = {
            'trainers': Trainer.objects.all(),
            'pokemons': Pokemon.objects.all()
        }
        return context