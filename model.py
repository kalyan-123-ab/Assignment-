from django.db import models
from django.utils import timezone
from datetime import timedelta

class Order(models.Model):
    customer = models.CharField(max_length=100)
    order_date = models.DateField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def top_customers_last_6_months():
        six_months_ago = timezone.now() - timedelta(days=180)
        return (Order.objects.filter(order_date__gte=six_months_ago)
                .values('customer')
                .annotate(total_spent=models.Sum('total_amount'))
                .order_by('-total_spent')[:5])

# Example usage in a view
def top_customers_view(request):
    top_customers = Order.top_customers_last_6_months()
    return render(request, 'top_customers.html', {'top_customers': top_customers})
