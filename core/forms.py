from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model =Store
        fields = ['name', 'location', 'owner', 'description']