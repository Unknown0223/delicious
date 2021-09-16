from django import forms
from front.models import Followers


class FollowersForm(forms.ModelForm):
    class Meta:
        model = Followers
        fields = "__all__"
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
        }
