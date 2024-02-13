from django import forms
from .models import Contact

class TaskForm(forms.Form):
    d = forms.FloatField(label="Диаметр", min_value=0)
    a = forms.FloatField(label="Сторона", min_value=0)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "text", "email"] 
