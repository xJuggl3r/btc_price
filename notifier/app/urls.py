# App urls.py

from django.contrib import admin
from django.urls import path
from app.views import BitcoinPriceView

app_name = 'app'

urlpatterns = [
    path('', BitcoinPriceView.as_view(), name='home'),
]
