from django import forms

class CustomUserForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, label="Prénom")
    last_name = forms.CharField(max_length=30, required=True, label="Nom")
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")