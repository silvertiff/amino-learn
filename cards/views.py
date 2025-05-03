from django.shortcuts import render, redirect
from .models import AminoAcidCard
from .forms import AminoAcidCardForm

def card_list(request):
    cards = AminoAcidCard.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

def add_card(request):
    if request.method == 'POST':
        form = AminoAcidCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = AminoAcidCardForm()
    return render(request, 'cards/add_card.html', {'form': form})

def card_table(request):
    cards = AminoAcidCard.objects.all()
    return render(request, 'cards/card_table.html', {'cards': cards})

from django.shortcuts import render
from .models import AminoAcidCard

def anki_mode(request):
    cards = AminoAcidCard.objects.all()
    # Преобразуем объекты в словари
    cards_data = [
        {
            'name': card.name,
            'structure': card.structure,
            'code': card.code,
        }
        for card in cards
    ]
    return render(request, 'cards/anki_mode.html', {'cards': cards_data})

