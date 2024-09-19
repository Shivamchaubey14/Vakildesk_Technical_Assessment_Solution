from django.db import models
from django.utils import timezone
from django.db.models import Sum, Max
from django.db.models.functions import Coalesce
from datetime import timedelta

class Order(models.Model):
    customer = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def top_5_customers(cls):
        six_months_ago = timezone.now() - timedelta(days=180)
        return (cls.objects.filter(order_date__gte=six_months_ago)
                           .values('customer')
                           .annotate(
                               total_spent=Sum('total_amount'),
                               most_recent_order_date=Coalesce(Max('order_date'), timezone.now())
                           )
                           .order_by('-total_spent')[:5])
