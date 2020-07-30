from django import forms


class Form(forms.Form):
    url = forms.CharField(max_length=250)
    hash = forms.CharField(max_length=15)
