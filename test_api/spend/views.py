from django.db.models import Sum, F
from rest_framework.generics import ListAPIView

from .models import SpendStatistic, SpendStatisticSerializer


class SpendStatisticView(ListAPIView):
    queryset = (
        SpendStatistic.objects
            .annotate(
                revenue=F('revenuestatistic__revenue')
            )
            .values('date', 'name')
            .order_by('-date', '-name')
            .annotate(
                total_spend=Sum('spend'),
                total_impressions=Sum('impressions'),
                total_clicks=Sum('clicks'),
                total_conversion=Sum('conversion'),
                total_revenue=Sum('revenue')
            )
            .values(
                'date',
                'name',
                'total_spend',
                'total_impressions',
                'total_clicks',
                'total_conversion',
                'total_revenue'
            )
        )
    serializer_class = SpendStatisticSerializer

    def get_queryset(self):
        return self.queryset.all()
