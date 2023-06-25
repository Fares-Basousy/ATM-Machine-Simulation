from django import forms
from .models import Person
class modelform(forms.ModelForm):
    class Meta:
        model=Person
        fields=("person_name","person_pass","cash")



