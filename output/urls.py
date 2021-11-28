from django.urls import path
from output.views import (
    OutputListView,
    OutputProductListView,
)


urlpatterns = [
    path('', OutputListView.as_view(), name='index_output'),
    path('product/<int:product>', OutputProductListView.as_view(), name="output_product")
]