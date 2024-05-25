from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Ogloszenie
from django.db.models.functions import Lower

def dodaj_ogloszenie(request):
    if request.method == 'POST':
        tytul = request.POST.get('tytul')
        tresc = request.POST.get('tresc')
        if tytul and tresc:
            Ogloszenie.objects.create(tytul=tytul, tresc=tresc)
            return render(request, 'ogloszenia/dodaj_ogloszenie_success.html')
    return render(request, 'ogloszenia/dodaj_ogloszenie.html')

def wyswietl_ogloszenia(request):
    tytul = request.GET.get('tytul', '')
    if tytul:
        ogloszenia = Ogloszenie.objects.filter(tytul__icontains=tytul)
    else:
        ogloszenia = Ogloszenie.objects.all()
    return render(request, 'ogloszenia/wyswietl_ogloszenia.html', {'ogloszenia': ogloszenia})

def edytuj_ogloszenie(request, ogloszenie_id):
    ogloszenie = get_object_or_404(Ogloszenie, pk=ogloszenie_id)
    if request.method == 'POST':
        tytul = request.POST.get('tytul')
        tresc = request.POST.get('tresc')
        ogloszenie.tytul = tytul
        ogloszenie.tresc = tresc
        ogloszenie.save()
        return redirect('wyswietl_ogloszenia')
    return render(request, 'ogloszenia/edytuj_ogloszenie.html', {'ogloszenie': ogloszenie})

def strona_glowna(request):
    return redirect('wyswietl_ogloszenia')

def usunieto_ogloszenie(request):
    return render(request, 'ogloszenia/usunieto_ogloszenie.html')   

def usun_ogloszenie(request, ogloszenie_id):
    try:
        ogloszenie = Ogloszenie.objects.get(pk=ogloszenie_id)
        ogloszenie.delete()
        return redirect('usunieto_ogloszenie')
    except Ogloszenie.DoesNotExist:
        return JsonResponse({'error': 'Ogłoszenie o podanym ID nie istnieje.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def wyswietl_ogloszenie(request, ogloszenie_id):
    ogloszenie = get_object_or_404(Ogloszenie, pk=ogloszenie_id)
    return render(request, 'ogloszenia/wyswietl_ogloszenie.html', {'ogloszenie': ogloszenie})


def sortuj_ogloszenia(request, kryterium):
    if kryterium == 'tytul':
        ogloszenia = Ogloszenie.objects.annotate(lower_tytul=Lower('tytul')).order_by('lower_tytul')
    elif kryterium == 'data':
        ogloszenia = Ogloszenie.objects.order_by('-data_publikacji')
    else:
        return JsonResponse({'error': 'Nieprawidłowe kryterium sortowania.'}, status=400)
    
    return render(request, 'ogloszenia/wyswietl_ogloszenia.html', {'ogloszenia': ogloszenia})

def wyszukaj_ogloszenia(request):
    tytul = request.GET.get('tytul', '')
    ogloszenia = Ogloszenie.objects.filter(tytul__icontains=tytul)
    return render(request, 'ogloszenia/wyszukaj_ogloszenia.html', {'ogloszenia': ogloszenia})