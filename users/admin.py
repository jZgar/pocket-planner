from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')  # Champs affichés dans la liste des utilisateurs
    search_fields = ('username', 'email')  # Champs par lesquels rechercher
    list_filter = ('is_staff', 'is_active')  # Filtres sur la liste des utilisateurs
    ordering = ('username',)  # Ordre par défaut

# Alternative (si tu préfères sans décorateur)
# admin.site.register(CustomUser, CustomUserAdmin)
