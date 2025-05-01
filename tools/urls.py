# tools/urls.py

from django.urls import path
from .views import (
    calculators_home,
    emi_view, sip_view, fd_view, rd_view,
    retirement_view, home_loan_view,
    cc_interest_view, taxable_income_view,
    budget_view, net_worth_view,
)

app_name = 'tools'

urlpatterns = [
    path('',       calculators_home,    name='index'),
    path('emi/',   emi_view,             name='emi'),
    path('sip/',   sip_view,             name='sip'),
    path('fd/',    fd_view,              name='fd'),
    path('rd/',    rd_view,              name='rd'),
    path('retirement/', retirement_view, name='retirement'),
    path('home-loan/',  home_loan_view,  name='home-loan'),
    path('cc-interest/', cc_interest_view, name='cc-interest'),
    path('taxable-income/', taxable_income_view, name='taxable-income'),
    path('budget/',        budget_view,       name='budget'),
    path('net-worth/',     net_worth_view,    name='net-worth'),
]
