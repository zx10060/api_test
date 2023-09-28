from django.db import models
from rest_framework import serializers


class SpendStatistic(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    spend = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    conversion = models.IntegerField(default=0)


class SpendStatisticSerializer(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.DateField()
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)

