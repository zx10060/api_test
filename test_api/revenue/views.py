from django.db.models import Sum
from rest_framework.generics import ListAPIView
from .models import RevenueStatistic, RevenueStatisticSerializer


class RevenueStatisticView(ListAPIView):
    queryset = (
        RevenueStatistic.objects
            .select_related('spend')
            .values('date', 'name')
            .order_by('-date', '-name')
            .annotate(
                total_revenue=Sum('revenue'),
                total_spend=Sum('spend__spend'),
                total_impressions=Sum('spend__impressions'),
                total_clicks=Sum('spend__clicks'),
                total_conversion=Sum('spend__conversion')
            )
            .values(
                'date',
                'name',
                'total_revenue',
                'total_spend',
                'total_impressions',
                'total_clicks',
                'total_conversion'
            )
    )
    serializer_class = RevenueStatisticSerializer

    def get_queryset(self):
        return self.queryset.all()
