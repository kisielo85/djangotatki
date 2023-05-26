from django import forms
from .models import Notatka

class addNoteForm(forms.ModelForm):
    class Meta:
        model = Notatka
        fields = ['title', 'content']


class editNoteForm(forms.ModelForm):
    class Meta:
        model = Notatka
        fields = ['title', 'content']