# admin.py

from django.contrib import admin
from .models import Ogloszenie

@admin.register(Ogloszenie)
class OgloszenieAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'tresc', 'data_publikacji')  # Wyświetl te pola w liście ogłoszeń w panelu admina
    list_filter = ('data_publikacji',)  # Dodaj możliwość filtrowania ogłoszeń po dacie publikacji
    search_fields = ('tytul', 'tresc')  # Dodaj pole wyszukiwania
