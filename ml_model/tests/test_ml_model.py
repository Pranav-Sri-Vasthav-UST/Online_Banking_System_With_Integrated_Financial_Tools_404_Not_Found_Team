import os
import pickle
import pandas as pd
import numpy as np
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class TestMLModelIntegration(TestCase):
    def setUp(self):
        # Create a test user and log in
        self.user = User.objects.create_user(
            username='mltester',
            password='testpass123',
            user_type='customer'
        )
        self.client = Client()
        self.client.login(username='mltester', password='testpass123')
        # Load the pickled model
        model_path = os.path.join(settings.BASE_DIR, 'ml_model', 'loan_amount_model.pkl')
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def test_model_loaded(self):
        # Ensure model has predict method
        self.assertTrue(hasattr(self.model, 'predict'))

    def test_model_prediction_output(self):
        # Prepare test input matching feature_names_in_
        feature_names = list(self.model.feature_names_in_)
        # Dummy data: use arbitrary positive values
        values = [30, 50000.0, 700, 5, 0.0, 0]
        df = pd.DataFrame([values], columns=feature_names)
        pred = self.model.predict(df)
        # Accept numpy array, list, or pandas Series
        self.assertTrue(isinstance(pred, (np.ndarray, list, pd.Series)))
        # Single prediction > 0
        amount = float(pred[0])
        self.assertGreater(amount, 0.0)

    def test_predict_view_get(self):
        url = reverse('ml_model:predict-loan')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '<form')

    def test_predict_view_post(self):
        url = reverse('ml_model:predict-loan')
        data = {
            'age': 30,
            'monthly_income': '50000',
            'credit_score': 700,
            'loan_tenure_years': 5,
            'existing_loan': '0',
            'dependents': 0,
        }
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)
        # Check that the result header appears
        self.assertContains(resp, 'Estimated Amount:')
