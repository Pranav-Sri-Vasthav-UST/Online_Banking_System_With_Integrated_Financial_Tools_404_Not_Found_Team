# tools/views.py

from django.shortcuts import render
# Removed login_required to allow public access

from .forms import (
    EMICalculatorForm, SIPCalculatorForm, FDCalculatorForm, RDCalculatorForm,
    RetirementCalculatorForm, HomeLoanEligibilityForm, CreditCardInterestForm,
    TaxableIncomeForm, BudgetForm, NetWorthForm
)
from .finance_tools import (
    calculate_emi, calculate_sip, calculate_fd, calculate_rd,
    calculate_retirement, calculate_home_loan_eligibility,
    calculate_credit_card_interest, calculate_taxable_income,
    calculate_budget, calculate_net_worth
)


def handle_calculator(request, form_class, calc_func, template_name):
    """
    Generic view handler for calculators. Accessible without login.
    """
    result = None
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            result = calc_func(**form.cleaned_data)
    else:
        form = form_class()
    return render(request, template_name, {'form': form, 'result': result})


def calculators_home(request):
    """
    GET /tools/ → show grid of all calculators (public)
    """
    calculators = [
        {'name': 'EMI Calculator',      'url_name': 'tools:emi'},
        {'name': 'SIP Calculator',      'url_name': 'tools:sip'},
        {'name': 'FD Calculator',       'url_name': 'tools:fd'},
        {'name': 'RD Calculator',       'url_name': 'tools:rd'},
        {'name': 'Retirement Estimator','url_name': 'tools:retirement'},
        {'name': 'Home Loan Estimator', 'url_name': 'tools:home-loan'},
        {'name': 'CC Interest',        'url_name': 'tools:cc-interest'},
        {'name': 'Taxable Income',     'url_name': 'tools:taxable-income'},
        {'name': 'Budget Planner',     'url_name': 'tools:budget'},
        {'name': 'Net Worth Calculator','url_name': 'tools:net-worth'},
    ]
    return render(request, 'tools/index.html', {'calculators': calculators})


def emi_view(request):
    return handle_calculator(request, EMICalculatorForm, calculate_emi, 'tools/emi.html')


def sip_view(request):
    return handle_calculator(request, SIPCalculatorForm, calculate_sip, 'tools/sip.html')


def fd_view(request):
    return handle_calculator(request, FDCalculatorForm, calculate_fd, 'tools/fd.html')


def rd_view(request):
    return handle_calculator(request, RDCalculatorForm, calculate_rd, 'tools/rd.html')


def retirement_view(request):
    return handle_calculator(request, RetirementCalculatorForm, calculate_retirement, 'tools/retirement.html')


def home_loan_view(request):
    return handle_calculator(request, HomeLoanEligibilityForm, calculate_home_loan_eligibility, 'tools/home_loan.html')


def cc_interest_view(request):
    return handle_calculator(request, CreditCardInterestForm, calculate_credit_card_interest, 'tools/cc_interest.html')


def taxable_income_view(request):
    return handle_calculator(request, TaxableIncomeForm, calculate_taxable_income, 'tools/taxable_income.html')


def budget_view(request):
    return handle_calculator(request, BudgetForm, calculate_budget, 'tools/budget.html')


def net_worth_view(request):
    return handle_calculator(request, NetWorthForm, calculate_net_worth, 'tools/net_worth.html')
