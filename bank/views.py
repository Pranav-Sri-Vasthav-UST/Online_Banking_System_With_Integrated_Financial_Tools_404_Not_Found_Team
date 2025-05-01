import json
from decimal import Decimal, InvalidOperation

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Account, Transaction
from .forms import AmountForm

@login_required
def balance_view(request):
    """
    GET /bank/balance/
    Render the current balance for the logged-in customer.
    """
    # Get or create account
    acct, _ = Account.objects.get_or_create(user=request.user)
    return render(request, 'bank/balance.html', {
        'balance': acct.balance
    })

@login_required
def deposit_view(request):
    """
    GET  /bank/deposit/   -> show form
    POST /bank/deposit/   -> process deposit and redirect to balance
    """
    form = AmountForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        amt = form.cleaned_data['amount']
        acct, _ = Account.objects.get_or_create(user=request.user)
        acct.balance += amt
        acct.save()
        Transaction.objects.create(account=acct, type=Transaction.DEPOSIT, amount=amt)
        return redirect('bank:balance')
    return render(request, 'bank/deposit.html', {'form': form})

@login_required
def withdraw_view(request):
    """
    GET  /bank/withdraw/  -> show form
    POST /bank/withdraw/  -> process withdrawal and redirect to balance
    """
    form = AmountForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        amt = form.cleaned_data['amount']
        acct, _ = Account.objects.get_or_create(user=request.user)
        if amt > acct.balance:
            form.add_error('amount', 'Insufficient funds.')
        else:
            acct.balance -= amt
            acct.save()
            Transaction.objects.create(account=acct, type=Transaction.WITHDRAW, amount=amt)
            return redirect('bank:balance')
    return render(request, 'bank/withdraw.html', {'form': form})

@login_required
def employee_customers_view(request):
    """
    GET /bank/employees/customers/
    Lists every customer and their current balance.
    """
    if not request.user.is_employee:
        return HttpResponseForbidden("You do not have access to this page.")
    customers = Account.objects.filter(
        user__user_type=Account._meta.get_field('user').remote_field.model.CUSTOMER
    ).select_related('user')
    return render(request, 'bank/employee_customers.html', {
        'customers': customers
    })


@login_required
def vault_balance_view(request):
    """
    GET /bank/employees/vault/
    Shows the sum of all account balances.
    """
    if not request.user.is_employee:
        return HttpResponseForbidden("You do not have access to this page.")
    total = Account.objects.aggregate(
        total_balance=Sum('balance')
    )['total_balance'] or Decimal('0.00')
    return render(request, 'bank/vault_balance.html', {
        'total_balance': total
    })


@login_required
def transaction_records_view(request):
    """
    GET /bank/employees/transactions/
    Displays all deposit/withdrawal transactions.
    """
    if not request.user.is_employee:
        return HttpResponseForbidden("You do not have access to this page.")
    transactions = Transaction.objects.select_related(
        'account__user'
    ).order_by('-timestamp')
    return render(request, 'bank/transaction_records.html', {
        'transactions': transactions
    })