from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.conf import settings
from .forms import ContactForm
from .tasks import send_custom_email


client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
# Create your views here.

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            razorpay_order_id = data.get("order_id")
            razorpay_payment_id = data.get("payment_id")
            razorpay_signature = data.get("signature")

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }

            # This raises SignatureVerificationError if the signature is invalid
            client.utility.verify_payment_signature(params_dict)

            # If verification passes, you can save the payment details here
            return JsonResponse({"verified": True})

        except razorpay.errors.SignatureVerificationError as e:
            print("Signature verification failed:", str(e))
            return JsonResponse({"verified": False}, status=400)
        except Exception as e:
            print("Unexpected error:", str(e))
            return JsonResponse({"error": "Server error"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=405)


class Home(TemplateView):
    def get(self,request):
        page = models.HomePage.objects.first()
        title = "Home"
        return render(request,'home.html',{"title":title,"page":page})

def about_us(request):
    title = "About Us"
    page = models.AboutPage.objects.first()
    return render(request,'about_us.html',{"title":title,"page":page})

def contact_us(request):
    title = "Contact Us"
    page = models.ContactPage.objects.first()
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Handle the cleaned data, e.g., send an email
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']

        send_custom_email.delay(f'Received a message from {name}', f"user info : mobile number: {phone} email: {email} \n message : " + message,recipient_list=[settings.EMAIL_HOST_USER],from_email=settings.EMAIL_HOST_USER)
        form = ContactForm()  # Reset the form after successful submission
        return render(request,'contact_us.html',{"title":title,"page":page,"form": form,"success": True})
    
    return render(request,'contact_us.html',{"title":title,"page":page,"form": form})

def beginner_to_pro(request):
    title = "Beginner to Pro pack"
    page = models.BeginnerToProPage.objects.first()
    return render(request,'beginner_to_pro.html',{"title":title,"page":page})

def fast_track_training(request):
    title = "Fast Track Training Pack"
    page = models.FastTrackTrainingPage.objects.first()
    return render(request,'fast_track_training.html',{"title":title,"page":page})

def workshops(request):
    title = "Workshops"
    page = models.WorkshopsPage.objects.first()
    return render(request,'workshops.html',{"title":title,"page":page})

def live_session(request):
    title = "Live Session"
    page = models.LiveSessionPage.objects.first()
    return render(request,'live_session.html',{"title":title,"page":page})

def skill_to_trainer(request):
    title = "Skill To Trainer Pack"
    page = models.SkillToTrainPage.objects.first()
    return render(request,'skill_to_trainer.html',{"title":title,"page":page})

def ultimage_trainer_launch_pack(request):
    title = "Ultimate Trainer Launch Pack"
    page = models.UltimateTrainerLaunchPackPage.objects.first()
    return render(request,'ultimage_trainer_launch_pack.html',{"title":title,"page":page})

def advanced_lead_generation_package(request):
    title = "Advanced Lead Generation Pack"
    page = models.AdvancedLeadGenerationPackage.objects.first()
    return render(request,'advanced_lead_generation_package.html',{"title":title,"page":page})

