from django.urls import path
from input.views import (
    InputListView,
    InputProductListView
)


urlpatterns = [
    path('', InputListView.as_view(), name='index_input'),
    path('product/<int:product>', InputProductListView.as_view(), name="input_product")
]