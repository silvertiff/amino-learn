from django.urls import path
from . import views  # Важно: импортим views ИЗ ТЕКУЩЕГО (.) каталога

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('add/', views.add_card, name='add_card'),
    path('table/', views.card_table, name='card_table'),
    path('anki/', views.anki_mode, name='anki_mode'),
]
