
from .models import DailyPrice
from rest_framework import serializers

class DailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrice
        fields = '__all__'
