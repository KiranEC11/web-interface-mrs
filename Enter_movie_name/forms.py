from django import forms

class TitleForm(forms.Form):
    Title = forms.CharField(
        max_length=100, 
            widget=forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Movie Name"
        })
    )