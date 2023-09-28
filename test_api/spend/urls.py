from django.urls import path
from .views import SpendStatisticView


urlpatterns = [
    path('', SpendStatisticView.as_view(), name='spend-statistic'),
]
