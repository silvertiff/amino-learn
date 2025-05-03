from django import forms
from .models import AminoAcidCard

class AminoAcidCardForm(forms.ModelForm):
    class Meta:
        model = AminoAcidCard
        fields = ['name', 'structure', 'code', 'image']
