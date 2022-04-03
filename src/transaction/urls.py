from django.urls import path
from transaction.views import (
    TransactionListView,
    TransactionCreateView,
)


urlpatterns = [
    path('', TransactionListView.as_view(), name='index_transaction'),
    path('create/',
        TransactionCreateView.as_view(), name='create_transaction'),
]