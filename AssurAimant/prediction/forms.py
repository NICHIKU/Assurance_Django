from django import forms

class PredictionForm(forms.Form):
    age = forms.Field(required=True, label="Age")
    children = forms.IntegerField(required=True, label="Nombre d'enfants", max_value=20)
    height = forms.FloatField(required=True, label="Taille", max_value=230)
    weight = forms.FloatField(required=True, label="Poids", min_value=20, max_value=250)
    smoker = forms.ChoiceField(label="Fumez-vous ?", choices=(
        ("yes", "Oui"),
        ("no", "Non"),
    ))
    sex = forms.ChoiceField(label="Sexe", choices=(
        ("male", "Homme"),
        ("female", "Femme"),
    ))
    region = forms.ChoiceField(label="Région", choices=(
        ("northeast", "Nord-est"),
        ("northwest", "Nord-ouest"),
        ("southeast", "Sud-est"),
        ("southwest", "Sud-ouest"),
    ))