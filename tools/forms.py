# tools/forms.py

from django import forms

class EMICalculatorForm(forms.Form):
    principal     = forms.FloatField(min_value=0, label='Principal (P)')
    annual_rate   = forms.FloatField(min_value=0, label='Annual Interest Rate (%)')
    months        = forms.IntegerField(min_value=1, label='Tenure (n) in months')

class SIPCalculatorForm(forms.Form):
    monthly_investment = forms.FloatField(min_value=0, label='Monthly Investment (P)')
    annual_rate        = forms.FloatField(min_value=0, label='Annual Interest Rate (%)')
    months             = forms.IntegerField(min_value=1, label='Number of months (n)')

class FDCalculatorForm(forms.Form):
    principal   = forms.FloatField(min_value=0, label='Principal (P)')
    annual_rate = forms.FloatField(min_value=0, label='Annual Interest Rate (%)')
    years       = forms.IntegerField(min_value=0, label='Years (t)')

class RDCalculatorForm(forms.Form):
    monthly_deposit = forms.FloatField(min_value=0, label='Monthly Deposit (P)')
    annual_rate     = forms.FloatField(min_value=0, label='Annual Interest Rate (%)')
    months          = forms.IntegerField(min_value=1, label='Number of months (n)')

class RetirementCalculatorForm(forms.Form):
    current_savings     = forms.FloatField(min_value=0, label='Current Savings')
    monthly_contribution = forms.FloatField(min_value=0, label='Monthly Contribution')
    annual_rate         = forms.FloatField(min_value=0, label='Annual Rate (%)')
    years               = forms.IntegerField(min_value=0, label='Years')

class HomeLoanEligibilityForm(forms.Form):
    monthly_income   = forms.FloatField(min_value=0, label='Monthly Income')
    monthly_expenses = forms.FloatField(min_value=0, label='Monthly Expenses')
    multiplier        = forms.FloatField(min_value=0, label='Multiplier (months*rate)', initial=60)

class CreditCardInterestForm(forms.Form):
    balance             = forms.FloatField(min_value=0, label='Current Balance')
    annual_rate         = forms.FloatField(min_value=0, label='Annual Interest Rate (%)')
    min_payment_percent = forms.FloatField(min_value=0, label='Minimum Payment Percent')

class TaxableIncomeForm(forms.Form):
    annual_income = forms.FloatField(min_value=0, label='Annual Income')
    deductions    = forms.FloatField(min_value=0, label='Total Deductions')

class BudgetForm(forms.Form):
    income   = forms.FloatField(min_value=0, label='Monthly Income')
    expenses = forms.FloatField(min_value=0, label='Monthly Expenses')

class NetWorthForm(forms.Form):
    assets      = forms.FloatField(min_value=0, label='Total Assets')
    liabilities = forms.FloatField(min_value=0, label='Total Liabilities')
