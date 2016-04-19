
from django import forms
from register.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'lastname', 'about']

