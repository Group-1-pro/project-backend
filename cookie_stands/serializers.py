from rest_framework import serializers
from .models import CookieStand


class CookieStandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStand
        fields = ['id', 'location', 'owner', 'description', 'hourly_sales', 'minimum_customers_per_hour', 'maximum_customers_per_hour', 'average_cookies_per_sale']

