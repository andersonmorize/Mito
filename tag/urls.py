from django.urls import path
from tag.views import (
    TagListView,
    TagCreateView,
    TagUpdateView,
)


urlpatterns = [
    path('', TagListView.as_view(), name='index_tag'),
    path('create', TagCreateView.as_view(), name='create_tag'),
    path('<pk>/update', TagUpdateView.as_view(), name='update_tag')
]