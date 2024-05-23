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


from django.core.paginator import Paginator
from .models import Ogloszenie


def wyswietl_ogloszenia(request):
    ogloszenia_lista = Ogloszenie.objects.all()
    paginator = Paginator(ogloszenia_lista,
                          request.GET.get('na_strone', 10))  # Domyślnie pokazuje 10 ogłoszeń na stronie

    page_number = request.GET.get('strona')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ogloszenia/wyswietl_ogloszenia.html', {'page_obj': page_obj})


def edytuj_ogloszenie(request, ogloszenie_id):
    ogloszenie = get_object_or_404(Ogloszenie, pk=ogloszenie_id)
    if request.method == 'POST':
        tytul = request.POST.get('tytul')
        tresc = request.POST.get('tresc')
        if tytul:
            ogloszenie.tytul = tytul
        if tresc:
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


def zlicz_ogloszenia(request):
    liczba_ogloszen = Ogloszenie.objects.count()
    return JsonResponse({'liczba_ogloszen': liczba_ogloszen})