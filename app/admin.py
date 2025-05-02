from django.contrib import admin
from . import models

admin.site.register(models.HomePage)
admin.site.register(models.ContactPage)
admin.site.register(models.UltimateTrainerLaunchPackPage)
admin.site.register(models.FastTrackTrainingPage)
admin.site.register(models.WorkshopsPage)
admin.site.register(models.LiveSessionPage)
admin.site.register(models.BeginnerToProPage)
admin.site.register(models.AboutPage)
admin.site.register(models.SkillToTrainPage)
admin.site.register(models.AdvancedLeadGenerationPackage)

class PagelinksAdmin(admin.ModelAdmin):
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