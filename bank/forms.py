from django import forms

class AmountForm(forms.Form):
    amount = forms.DecimalField(
        min_value=0.01,
        max_digits=12,
        decimal_places=2,
        label="Amount",
        widget=forms.NumberInput(attrs={'step': '0.01'})
    )