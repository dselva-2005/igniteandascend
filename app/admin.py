from django.contrib import admin
from . import models

from django.contrib import admin
from django.utils.html import format_html
from django.shortcuts import redirect
from django.contrib import messages
from django.db import models as dj_models

def clone_model(modeladmin, request, queryset):
    for obj in queryset:
        # Make a copy
        obj.pk = None
        obj.save()
    model_name = queryset.model._meta.verbose_name_plural.title()
    messages.success(request, f"Selected {model_name} successfully cloned.")
clone_model.short_description = "Clone selected instances"

class CloneableAdmin(admin.ModelAdmin):
    actions = [clone_model]

admin.site.register(models.HomePage, CloneableAdmin)
admin.site.register(models.ContactPage, CloneableAdmin)
admin.site.register(models.UltimateTrainerLaunchPackPage, CloneableAdmin)
admin.site.register(models.FastTrackTrainingPage, CloneableAdmin)
admin.site.register(models.WorkshopsPage, CloneableAdmin)
admin.site.register(models.LiveSessionPage, CloneableAdmin)
admin.site.register(models.BeginnerToProPage, CloneableAdmin)
admin.site.register(models.AboutPage, CloneableAdmin)
admin.site.register(models.SkillToTrainPage, CloneableAdmin)
admin.site.register(models.AdvancedLeadGenerationPackage, CloneableAdmin)


class PagelinksAdmin(admin.ModelAdmin):
    actions = [clone_model]
    # Define which fields you want to display
    list_display = ('title1','title2','title3','title4',
        'product1name', 'product1url',
        'product2name', 'product2url',
        'product3name', 'product3url',
        'product4name', 'product4url',
        'product5name', 'product5url',
        'product6name', 'product6url',
        'product7name', 'product7url',
        'product8name', 'product8url',
        'product9name', 'product9url',
    )
    
    # Limit the number of fields in the form view
    fields = ('title1','title2','title3','title4',
        'product1name', 'product1url',
        'product2name', 'product2url',
        'product3name', 'product3url',
        'product4name', 'product4url',
        'product5name', 'product5url',
        'product6name', 'product6url',
        'product7name', 'product7url',
        'product8name', 'product8url',        
        'product9name', 'product9url',

    )

# Register the custom admin for ProductLinks
admin.site.register(models.Pagelinks, PagelinksAdmin)