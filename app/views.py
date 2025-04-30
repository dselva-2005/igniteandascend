from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

# Create your views here.
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
    return render(request,'contact_us.html',{"title":title,"page":page})

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