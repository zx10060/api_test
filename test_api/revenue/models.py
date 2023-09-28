from django.db import models
from rest_framework import serializers


class RevenueStatistic(models.Model):
    name = models.CharField(max_length=255)
    spend = models.ForeignKey('spend.SpendStatistic', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    revenue = models.DecimalField(max_digits=9, decimal_places=2, default=0)


class RevenueStatisticSerializer(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.DateField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()
