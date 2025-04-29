from django.urls import path
from .views import Books


app_name = 'books'  # This is necessary for namespacing

urlpatterns = [
    path('',Books.as_view(),name='book-list')
]