from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
    widget=forms.TextInput(
        attrs={
            'class': 'classe-a classe-b',
            'placeholder': 'Aqui veio do init',
        }
    ),
    label='Primeiro Nome',
    help_text='Texto de ajuda para seu usuário',
    )
    
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone", 'email', 'description', 'category')

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if first_name == "ABC":
            raise ValidationError("" "Não digite ABC neste campo", code="Inválido")
        return first_name
