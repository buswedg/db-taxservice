from django.urls import path

from apps.tax import api_views

app_name = "tax"

urlpatterns = [

    path('taxrate/bypostcode/', api_views.TaxRateByZipView.as_view(), name='tax_rate'),

]
