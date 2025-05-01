import json
import razorpay
import traceback
from django.conf import settings
from django.views.generic import ListView
from books.models import Book,BookPage
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from books.models import Book, Purchase
from django.utils import timezone
import mimetypes
import requests

def verify_payment_on_rzp(payment_id):
    """Checks if a Razorpay payment is completed (captured)."""
    auth = (settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
    response = requests.get(f"https://api.razorpay.com/v1/payments/{payment_id}", auth=auth)

    if response.status_code == 200:
        data = response.json()
        return data.get("status") == "captured"
    return False

@csrf_exempt
@login_required
def verify_and_capture_payment(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            payment_id = data.get("payment_id")
            order_id = data.get("order_id")
            book_id = data.get("book_id")

            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

            # 1. Verify the payment exists
            payment = client.payment.fetch(payment_id)

            # 2. Optionally verify the signature (recommended for high security)
            # Skipping here for brevity

            # 3. Capture the payment
            amount = payment["amount"]
            client.payment.capture(payment_id, amount)

            # 4. Grant access: create Purchase record
            book = Book.objects.get(id=book_id)
            Purchase.objects.create(user=request.user, book=book, purchased_at=timezone.now())

            return JsonResponse({"status": "success", "message": "Payment captured and access granted."})

        except Exception as e:
            traceback.print_exc()
            return JsonResponse({"status": "error", "message": str(e)}, status=500)



def serve_paywalled_media(request, path):
    payment_id = request.GET.get('payment_id')

    if not payment_id or not verify_payment_on_rzp(payment_id):
        return HttpResponseForbidden("Access Denied: Invalid or missing payment.")

    file_path = f'/home/dselva/python_projects/professional_order_1/protected/{path}'
    content_type, _ = mimetypes.guess_type(file_path)

    response = HttpResponse()
    response['Content-Type'] = content_type or 'application/octet-stream'
    response['X-Accel-Redirect'] = f'/protected_internal/{path}'  # Nginx will serve the file
    return response


def create_razorpay_order(request):
    if request.method == "POST":
        try:
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            data = json.loads(request.body)

            amount = int(data.get('amount', 50000))  # ₹500 in paisa
            order = client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture": 1
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
        context['page'] = BookPage.objects.first()
        context['RAZORPAY_KEY_ID'] = settings.RAZOR_KEY_ID
        context['GOOGLE_CLIENT_ID'] = settings.GOOGLE_CLIENT_ID
        context['GOOGLE_APP_ID'] = settings.GOOGLE_APP_ID
        return context