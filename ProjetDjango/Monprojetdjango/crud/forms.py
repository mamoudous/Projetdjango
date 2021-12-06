from django import forms
from .models import etudiant

class etudiantForm(forms.ModelForm):
    class Meta:
        model = etudiant
        fields = '__all__'