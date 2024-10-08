from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=CustomUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        # Envoyer un e-mail de bienvenue lors de la création d'un utilisateur
        send_mail(
            'Bienvenue sur PocketPlanner',
            f'Bonjour {instance.username},\n\nMerci de vous être inscrit sur PocketPlanner. Nous sommes ravis de vous compter parmi nous !',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )

@receiver(post_delete, sender=CustomUser)
def user_deleted(sender, instance, **kwargs):
    # Exemple : Logger la suppression d'un utilisateur
    print(f"L'utilisateur {instance.username} a été supprimé.")
