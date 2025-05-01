# ml_model/forms.py

from django import forms

class LoanPredictionForm(forms.Form):
    age = forms.IntegerField(min_value=18, label="Age (years)")
    monthly_income = forms.DecimalField(min_value=0, decimal_places=2, label="Monthly Income")
    credit_score = forms.IntegerField(min_value=300, max_value=850, label="Credit Score")
    loan_tenure_years = forms.IntegerField(min_value=1, label="Loan Tenure (years)")
    existing_loan = forms.DecimalField(min_value=0, decimal_places=2, label="Existing Loan Amount")
    dependents = forms.IntegerField(min_value=0, label="Number of Dependents")
