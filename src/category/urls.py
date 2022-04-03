from django.urls import path
from category.views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
)


urlpatterns = [
    path('', CategoryListView.as_view(), name='index_category'),
    path('create', CategoryCreateView.as_view(), name='create_category'),
    path('<pk>/update', CategoryUpdateView.as_view(), name='update_category')
]