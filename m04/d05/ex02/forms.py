from django import forms

class InputForm(forms.Form):
    text = forms.CharField(label='Enter text', max_length=200)   