from django.urls import path
from . import views


app_name = 'books'  # This is necessary for namespacing

urlpatterns = [
    path('',views.Books.as_view(),name='book-list'),
    path("create-order/", views.create_razorpay_order, name="create_razorpay_order")

]