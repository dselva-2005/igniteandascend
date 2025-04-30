from django.views.generic import ListView
from books.models import Book
import razorpay
from django.conf import settings
from django.http import JsonResponse
import json
import traceback

def create_razorpay_order(request):
    if request.method == "POST":
        try:
            print("Using key:", settings.RAZOR_KEY_ID)
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            data = json.loads(request.body)
            print("Received data:", data)

            amount = int(data.get('amount', 50000))  # ₹500 in paisa
            order = client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture": 0
            })

            return JsonResponse(order)

        except Exception as e:
            print("Exception occurred:")
            traceback.print_exc()
            return JsonResponse({"error": str(e)}, status=500)


    
class Books(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ebooks"
        context['RAZORPAY_KEY_ID'] = settings.RAZOR_KEY_ID
        return context