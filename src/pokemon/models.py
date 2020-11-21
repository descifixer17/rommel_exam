from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from trainer.models import Trainer

# Create your models here.

class Pokemon(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='pokemons')
    species = models.ForeignKey('Species', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0, 
                                    validators=[ 
                                        MinValueValidator(0),
                                        MaxValueValidator(100)
                                    ]
                                )
    
    def __str__(self):
        return self.name

class Species(models.Model):
    SPECIES_CHOICE = [
        ('bulbasaur', 'Bulbasaur'),
        ('charmander', 'Charmander'),
        ('squirtle', 'Squirtle'),
        ('unknown', 'unknown')
    ]

    FIRST_TYPE_CHOICE = [
        ('electric', 'Electric'),
        ('fire', 'Fire'),
        ('grass', 'Grass'),
        ('water', 'Water'),
        ('unknown', 'unknown')
    ]

    SECOND_TYPE_CHOICE = [
        ('ground', 'Ground'),
        ('flying', 'Flying'),
        ('poison', 'Poison'),
        ('unknown', 'unknown')
    ]

    name = models.CharField(max_length=50, choices=SPECIES_CHOICE, default='unknown')
    first_type = models.CharField(max_length=50, choices=FIRST_TYPE_CHOICE, default='unknown')
    second_type = models.CharField(max_length=50, choices=SECOND_TYPE_CHOICE, blank=True)

    class Meta:
        verbose_name_plural = 'Species'

    def __str__(self):
        return self.name
