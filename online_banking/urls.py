# online_banking/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Root → redirect to login (or change to profile/home view)
    path(
        '',
        RedirectView.as_view(pattern_name='accounts:login', permanent=False),
        name='home'
    ),

    # Account management
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # Banking operations
    path('bank/', include('bank.urls', namespace='bank')),

    # Finance tools calculators
    path('tools/', include('tools.urls', namespace='tools')),

    # ML loan estimator
    path('ml/', include('ml_model.urls', namespace='ml_model')),
]
