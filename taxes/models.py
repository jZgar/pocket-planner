from django.db import models

# Create your models here.


class CountryTax(models.Model):
    COUNTRY_CHOICES = [
        ('fr', 'France'),
    ]

    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, unique=True, help_text="Pays pour lequel la grille d'imposition est définie.")
    tax_brackets = models.JSONField(help_text="Grille d'imposition, sous forme de structure JSON pour une flexibilité accrue.")

    def __str__(self):
        return f"Grille d'imposition pour {self.country}"