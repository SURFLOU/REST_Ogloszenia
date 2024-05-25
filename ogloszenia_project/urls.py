from django.urls import path
from django.contrib import admin
from ogloszenia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.strona_glowna, name='strona_glowna'),
    path('dodaj/', views.dodaj_ogloszenie, name='dodaj_ogloszenie'),
    path('edytuj/<int:ogloszenie_id>/', views.edytuj_ogloszenie, name='edytuj_ogloszenie'),
    path('wyswietl/', views.wyswietl_ogloszenia, name='wyswietl_ogloszenia'),
    path('ogloszenia/<int:ogloszenie_id>/', views.usun_ogloszenie, name='usun_ogloszenie'),
    path('ogloszenia/usunieto/', views.usunieto_ogloszenie, name='usunieto_ogloszenie'),
    path('ogloszenia/szczegoly/<int:ogloszenie_id>/', views.wyswietl_ogloszenie, name='wyswietl_szczegoly_ogloszenia'),
    path('ogloszenia/sortuj/<str:kryterium>/', views.sortuj_ogloszenia, name='sortuj_ogloszenia'),
    path('ogloszenia/wyszukaj/', views.wyszukaj_ogloszenia, name='wyszukaj_ogloszenia'),
]
