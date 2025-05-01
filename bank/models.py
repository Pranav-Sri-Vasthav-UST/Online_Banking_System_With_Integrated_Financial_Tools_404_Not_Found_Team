# bank/models.py

from django.db import models
from django.conf import settings

class Account(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='account'
    )
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        help_text="Current account balance"
    )

    def __str__(self):
        return f"{self.user.username}'s account"

class Transaction(models.Model):
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    TYPE_CHOICES = [
        (DEPOSIT, 'Deposit'),
        (WITHDRAW, 'Withdraw'),
    ]
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_type_display().title()} of {self.amount} on {self.timestamp.date()}"
