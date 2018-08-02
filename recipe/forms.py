from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields = [
        'title',
        'steps',
        'picture'
        ]

class RawRecipeForm(forms.Form):
    title   = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'your title'}))
    steps   = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'your steps'}))
    picture = forms.ImageField()
    widget  = forms.CharField(
                label='Recipe Steps',
                widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Recipe Steps Here'
                })
    )
