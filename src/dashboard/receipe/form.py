from django import forms
from front.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "prep_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "cook_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "stars": forms.NumberInput(attrs={'class': 'form-control'}),
            "posted_at": forms.DateInput(attrs={'class': 'form-control'}),
        }