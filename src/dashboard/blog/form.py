from django import forms

from front.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={'class': 'form-control'},
            ),
            "short_description": forms.TextInput(
                attrs={'class': 'form-control'},
            ),
            "description": forms.TextInput(
                attrs={'class': 'form-control'},
            ),
            "image": forms.Media(
                media={'class': 'form-control'},
            ),
            "author": forms.Select(
                attrs={'class': 'form-control'}
            ),
            "posted_at": forms.DateInput(
                attrs={'class': 'form-control'},
            )
        }
