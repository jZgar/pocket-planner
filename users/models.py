from django.contrib.auth.models import AbstractUser
from django.db import models

from taxes.models import CountryTax


# Create your models here.
class CustomUser(AbstractUser):
    TAX_STATUS_CHOICES = [
        ('single', 'Célibataire'),
        ('married_joint', 'Marié - Déclaration conjointe'),
    ]

    RESIDENCE_COUNTRY_CHOICES = [
        ('fr', 'France'),
        ('be', 'Belgique'),
        ('ca', 'Canada'),
    ]

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    annual_income = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Revenu annuel de l'utilisateur.")
    tax_status = models.CharField(max_length=20, choices=TAX_STATUS_CHOICES, null=True, blank=True, help_text="Statut fiscal de l'utilisateur.")
    number_of_dependents = models.IntegerField(null=True, blank=True, help_text="Nombre de personnes à charge.")
    tax_residence_country = models.CharField(max_length=20, choices=RESIDENCE_COUNTRY_CHOICES, null=True, blank=True, help_text="Pays de résidence fiscale.")
    additional_income = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Revenus additionnels de l'utilisateur.")
    deductions = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Montant total des déductions fiscales.")
    tax_credits = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Montant des crédits d'impôt.")
    investment_income = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Montant des revenues en bourse si imposable (CTO)")

    tax_country = models.ForeignKey(CountryTax, on_delete=models.SET_NULL, null=True, blank=True,
                                    help_text="Grille d'imposition basée sur le pays.")

    def __str__(self):
        return self.username