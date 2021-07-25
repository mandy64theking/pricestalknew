from django import forms

class NameForm(forms.Form):
    URL2=forms.CharField()
    budget2=forms.IntegerField()
    email2=forms.CharField()