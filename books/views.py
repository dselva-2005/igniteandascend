from django.views.generic import ListView
from books.models import Book
import razorpay
from django.conf import settings
from django.http import JsonResponse
import json

client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def create_razorpay_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        amount = data.get('amount', 50000)  # in paisa (₹500)

        order = client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": 0
        })

        return JsonResponse(order)

    
class Books(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ebooks"
        context['RAZORPAY_KEY_ID'] = settings.RAZOR_KEY_ID
        return context