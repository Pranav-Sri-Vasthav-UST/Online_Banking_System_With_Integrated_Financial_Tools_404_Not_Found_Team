# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    EMPLOYEE = 'employee'
    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (EMPLOYEE, 'Employee'),
    ]
    user_type = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=CUSTOMER,
        help_text="Select whether you are a customer or an employee."
    )

    @property
    def is_customer(self):
        return self.user_type == self.CUSTOMER

    @property
    def is_employee(self):
        return self.user_type == self.EMPLOYEE
