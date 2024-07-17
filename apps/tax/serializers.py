from rest_framework import serializers
from apps.tax.models import TaxRate


class TaxRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxRate
        fields = ('id', 'state', 'zipcode', 'tax_region_name', 'estimated_combined_rate',
                  'state_rate', 'estimated_county_rate', 'estimated_city_rate',
                  'estimated_special_rate', 'risk_level')