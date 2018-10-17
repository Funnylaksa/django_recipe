from django import forms

from .models import Diary
from datetime import date


class DiaryModelForm(forms.ModelForm):
    class Meta:
        model=Diary
        fields= [
        'date',
        'title',
        'description'
        ]

    def __init__(self, *args, **kwargs):
        super(DiaryModelForm, self).__init__(*args, **kwargs)
        #self.fields['date'].widget.attrs['placeholder'] = date.today()
        self.fields['date'].initial = date.today()
