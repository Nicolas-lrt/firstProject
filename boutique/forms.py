from django import forms


class payChoiceForm(forms.Form):
    choices = (
        (1, "Carte Visa CashBack"),
        (2, "Monnaie Virtuelle")
    )
    choiceForm = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
