# serializers.py
from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['Country_id', 'country_name', 'country_code', 'description', 'logo_url', 'status']
    
class CountryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name', 'country_code', 'description', 'logo_url', 'status']
