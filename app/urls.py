from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    path("about/",views.about_us,name='about_us'),
    path("contact/",views.contact_us,name='contact_us'),
    path("workshops/",views.workshops,name='workshops'),
    path("live-session/",views.live_session,name='live_session'),
    path("beginner-to-pro/",views.beginner_to_pro,name='beginner_to_pro'),
    path("fast-track-training/",views.fast_track_training,name='fast_track_training'),
    path("skill-to-trainer/",views.skill_to_trainer,name='skill_to_trainer'),
    path("ultimate-trainer-launch-pack/",views.ultimage_trainer_launch_pack,name='ultimage_trainer_launch_pack'),
    path("advanced-lead-generation-package/",views.advanced_lead_generation_package,name='advanced_lead_generation_package'),
    path("",views.Home.as_view(),name='home_page'),
]