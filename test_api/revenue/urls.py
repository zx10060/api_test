from django.urls import path
from .views import RevenueStatisticView


urlpatterns = [
    path('', RevenueStatisticView.as_view(), name='revenue-statistic'),
]
