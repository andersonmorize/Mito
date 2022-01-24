from datetime import datetime, timedelta, date
import calendar
from django.utils import timezone


from django.db.models import Q, Sum

from django.views.generic.base import TemplateView
from product.models import Product

class DashboardIndex(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_products'] = Product.objects.all().count()
        context['count_products_active'] = Product.objects.filter(status=True).count()
        context['count_products_no_active'] = Product.objects.filter(status=False).count()

        return context

