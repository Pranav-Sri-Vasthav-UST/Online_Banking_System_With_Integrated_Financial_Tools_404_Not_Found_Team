from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal

from django.contrib.auth import get_user_model
from bank.models import Account, Transaction

User = get_user_model()

class TestBanking(TestCase):

    def setUp(self):
        # Create a test customer
        self.customer = User.objects.create_user(
            username="alice", password="pass1234", user_type="customer"
        )
        self.client = Client()

    def test_deposit_and_withdraw_flow(self):
        # Login
        self.assertTrue(self.client.login(username="alice", password="pass1234"))

        # Deposit ₹1000 via POST JSON
        resp = self.client.post(
            reverse('bank:deposit'),
            data='{"amount": 1000}',
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['balance'], 1000.0)

        # Withdraw ₹300
        resp = self.client.post(
            reverse('bank:withdraw'),
            data='{"amount": 300}',
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['balance'], 700.0)

        # Check Transaction records
        txs = Transaction.objects.filter(account__user=self.customer)
        self.assertEqual(txs.count(), 2)
        self.assertEqual(txs.first().type, Transaction.DEPOSIT)

    def test_balance_view(self):
        # Unauthenticated → should redirect to login
        resp = self.client.get(reverse('bank:balance'))
        self.assertEqual(resp.status_code, 302)

        # After login, returns JSON
        self.client.login(username="alice", password="pass1234")
        resp = self.client.get(reverse('bank:balance'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('balance', resp.json())

    def test_invalid_withdraw(self):
        self.client.login(username="alice", password="pass1234")
        # Withdraw with no balance
        resp = self.client.post(
            reverse('bank:withdraw'),
            data='{"amount": 100}',
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 400)
        self.assertIn('Insufficient', resp.json()['error'])
