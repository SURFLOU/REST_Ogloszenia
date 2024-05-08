from django.urls import path
from django.contrib import admin
from ogloszenia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.strona_glowna, name='strona_glowna'),
    path('dodaj/', views.dodaj_ogloszenie, name='dodaj_ogloszenie'),
    path('edytuj/<int:ogloszenie_id>/', views.edytuj_ogloszenie, name='edytuj_ogloszenie'),
    path('wyswietl/', views.wyswietl_ogloszenia, name='wyswietl_ogloszenia'),
]
