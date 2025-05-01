# bank/urls.py

from django.urls import path
from .views import (
    balance_view,
    deposit_view,
    withdraw_view,
    employee_customers_view,
    vault_balance_view,
    transaction_records_view,
)

app_name = 'bank'

urlpatterns = [
    # Customer endpoints (forms + JSON API)
    path('balance/',    balance_view,    name='balance'),
    path('deposit/',    deposit_view,   name='deposit'),
    path('withdraw/',   withdraw_view,  name='withdraw'),

    # Employee endpoints
    path('employees/customers/',    employee_customers_view,   name='employee_customers'),
    path('employees/vault/',        vault_balance_view,        name='vault_balance'),
    path('employees/transactions/', transaction_records_view,   name='transaction_records'),
]
