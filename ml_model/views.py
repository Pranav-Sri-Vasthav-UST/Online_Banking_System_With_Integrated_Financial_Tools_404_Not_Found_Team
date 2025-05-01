# ml_model/views.py

import os
import pickle

from django import shortcuts
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .forms import LoanPredictionForm
import pandas as pd

# Load model once at import
# MODEL_PATH = os.path.join(settings.BASE_DIR, "ml_model", "model.pkl")
with open(r"D:\Python Training\Online_Banking_System_With_Integrated_Financial_Tools_404_Not_Found_Team\ml_model\loan_amount_model.pkl", "rb") as f:
    model = pickle.load(f)

@login_required
@csrf_protect
def predict_view(request):
    """
    GET  → render form
    POST → validate, predict, render result
    """
    if request.method == "POST":
        form = LoanPredictionForm(request.POST)
        ctx = {'form': form, 'predicted_amount': None}
        if form.is_valid():
            data = form.cleaned_data
            features = [
                data["age"],
                float(data["monthly_income"]),
                data["credit_score"],
                data["loan_tenure_years"],
                float(data["existing_loan"]),
                data["dependents"],
            ]
            cols = model.feature_names_in_
            df_in = pd.DataFrame([features], columns=cols)
            predicted = model.predict(df_in)[0]
            ctx['predicted_amount'] = round(predicted, 2)
            return shortcuts.render(
                request,
                "ml_model/predict.html",
                {"form": form, "predicted_amount": round(predicted, 2)},
            )
            
    else:
        form = LoanPredictionForm()

    return shortcuts.render(request, "ml_model/predict.html", {"form": form})
