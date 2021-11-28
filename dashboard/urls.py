from django.urls import path
from dashboard.views import DashboardIndex


urlpatterns = [
    path('', DashboardIndex.as_view(), name='dashboard_index'),
]