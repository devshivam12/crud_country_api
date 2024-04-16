from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['Country_id', 'country_name', 'country_code', 'description', 'logo_url', 'status']

    def validate_country_name(self, value):
        # Add validation logic for country_name field
        # For example, ensuring that country name is not empty
        if not value:
            raise serializers.ValidationError("Country name cannot be empty.")
        return value

    def validate_country_code(self, value):
        # Add validation logic for country_code field
        # For example, ensuring that country code is in uppercase
        if not value.isupper():
            raise serializers.ValidationError("Country code must be in uppercase.")
        return value

    # Add more field-level validation methods as needed
class CountryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name', 'country_code']  

    def create(self, validated_data):
        return Country.objects.create(
            country_name=validated_data['country_name'],
            country_code=validated_data['country_code']
        )


class CountryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name', 'country_code']

    def validate_country_name(self, value):
        if not value:
            raise serializers.ValidationError("Country name cannot be empty.")
        return value

    def validate_country_code(self, value):
        if not value.isupper():
            raise serializers.ValidationError("Country code must be in uppercase.")
        return value






