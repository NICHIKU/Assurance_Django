from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class ModificationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Un utilisateur avec cet email existe déjà.")
        return email