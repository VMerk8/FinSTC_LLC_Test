from rest_framework import serializers

from .models import Car, Dealer, Manufacturer


class DealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dealer
        fields = ['id', 'dealer_name', 'address', 'email']


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'car_model', 'release_year', 'dealer_id', 'manufacturer_id']


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ['id', 'manufacturer_name']
