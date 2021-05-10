from django import forms

class name(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()