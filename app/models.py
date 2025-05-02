from django.db import models
from tinymce.models import HTMLField  # if using TinyMCE's HTMLField



class HomePage(models.Model):

    header_image = models.ImageField()  # add upload_to for better file management
    header_image_mobile = models.ImageField(null=True)  # add upload_to for better file management
    slide_image1 = models.ImageField()
    slide_image2 = models.ImageField()
    slide_image3 = models.ImageField()
    slide_image4 = models.ImageField()
    slide_image5 = models.ImageField()
    slide_image6 = models.ImageField()
    slide_image7 = models.ImageField()
    slide_image8 = models.ImageField()
    slide_image9 = models.ImageField()
    slide_image10 = models.ImageField()
    slide_image11 = models.ImageField()
    slide_image12 = models.ImageField()
    about_image = models.ImageField()
    about_content = HTMLField()
    htmlContent = HTMLField()
    our_service_image1 = models.ImageField()
    our_service_image2 = models.ImageField()
    our_service_image3 = models.ImageField()
    our_service_image4 = models.ImageField()
    our_service_image5 = models.ImageField()
    our_service_image6 = models.ImageField()
    review_image1 = models.ImageField()
    review_image2 = models.ImageField()
    review_image3 = models.ImageField()
    review_image4 = models.ImageField()
    review_image5 = models.ImageField()
    review_image6 = models.ImageField()
    review_image7 = models.ImageField()
    review_image8 = models.ImageField()
    review_image9 = models.ImageField()
    background_image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"HomePage updated on {self.updated}"


class AboutPage(models.Model):

    header_content = HTMLField()

    image_of_person1 = models.ImageField()
    html_content_for_person1 = HTMLField()

    image_of_person2 = models.ImageField()
    html_content_for_person2 = HTMLField()

    image_of_person3 = models.ImageField()
    html_content_for_person3 = HTMLField()

    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"AboutPage updated on {self.updated}"

class ContactPage(models.Model):
    header_image = models.ImageField()  # add upload_to for better file management
    htmlcontent = HTMLField()
    contact_us_html = HTMLField()
    form_upper_html = HTMLField()
    form_below_html = HTMLField()
    clarity_call_html = HTMLField()
    clarity_call_link = models.TextField()
    clarity_call_button = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"ContactPage updated on {self.updated}"


class BeginnerToProPage(models.Model):
    header_image = models.ImageField()  # add upload_to for better file management
    beginner_html_title = HTMLField()
    beginner_html = HTMLField()
    pro_html_title = HTMLField()
    pro_html = HTMLField()
    
    clarity_call_html1 = HTMLField()
    clarity_call_link1 = models.TextField()
    clarity_call_button1 = models.TextField()
    
    clarity_call_html2 = HTMLField()
    clarity_call_link2 = models.TextField()
    clarity_call_button2 = models.TextField()

    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"BeginnerToProPage updated on {self.updated}"


class LiveSessionPage(models.Model):
    header_html = HTMLField()
    header_image = models.ImageField()  # add upload_to for better file management
    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this
    faq_html = HTMLField()

    clarity_call_html1 = HTMLField()
    clarity_call_link1 = models.TextField()
    clarity_call_button1 = models.TextField()
    
    clarity_call_html2 = HTMLField()
    clarity_call_button2 = models.TextField()
    clarity_call_link2 = models.TextField()

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"LiveSessionPage updated on {self.updated}"


class SkillToTrainPage(models.Model):
    header_html = HTMLField()
    header_image = models.ImageField()  # add upload_to for better file management
    htmlcontent = HTMLField()
    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    clarity_call_link1 = models.TextField()
    clarity_call_html1 = HTMLField()
    clarity_call_button1 = models.TextField()

    htmlcontent2 = HTMLField()
    
    faq_html = HTMLField()


    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"SkillToTrainPage updated on {self.updated}"


class UltimateTrainerLaunchPackPage(models.Model):
    header_image = models.ImageField()  # add upload_to for better file management
    header_html = HTMLField()
    htmlcontent = HTMLField()

    clarity_call_link1 = models.TextField()
    clarity_call_html1 = HTMLField()
    clarity_call_button1 = models.TextField()

    content2 = HTMLField()

    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"UltimateTrainerLaunchPackPage updated on {self.updated}"


class WorkshopsPage(models.Model):
    header_image = models.ImageField()  # add upload_to for better file management
    htmlcontent = HTMLField()
    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this
    button = models.TextField(null=True)
    buttonurl =  models.URLField(null=True)
    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"WorkshopsPage updated on {self.updated}"

class AdvancedLeadGenerationPackage(models.Model):
    header_image = models.ImageField()  # add upload_to for better file management
    header_html = HTMLField()  # add upload_to for better file management
    htmlcontent = HTMLField()
    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    clarity_call_link1 = models.TextField()
    clarity_call_html1 = HTMLField()
    clarity_call_button1 = models.TextField()

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"WorkshopsPage updated on {self.updated}"


class FastTrackTrainingPage(models.Model):
    header_image = models.ImageField()  # add upload_to for better file management
    header_htmlcontent = HTMLField()

    nich_navigator_header1 = HTMLField()
    nich_navigator_header2 = HTMLField()
    nich_navigator_header_image = models.ImageField()
    nich_navigator_button1 = models.TextField()
    nich_navigator_button2 = models.TextField()
    nich_navigator_link1 = models.TextField()
    nich_navigator_link2 = models.TextField()
    nich_navigator_htmlcontent1 = HTMLField()
    nich_navigator_htmlcontent2 = HTMLField()

    meta_google_header1 = HTMLField()
    meta_google_header2 = HTMLField()
    meta_google_header_image = models.ImageField()
    meta_google_button1 = models.TextField()
    meta_google_link1 = models.TextField()
    meta_google_button2 = models.TextField()
    meta_google_link2 = models.TextField()
    meta_google_htmlcontent1 = HTMLField()
    meta_google_htmlcontent2 = HTMLField()

    instagram_seo_header1 = HTMLField()
    instagram_seo_header2 = HTMLField()
    instagram_seo_header_image = models.ImageField()
    instagram_seo_button1 = models.TextField()
    instagram_seo_link1 = models.TextField()
    instagram_seo_button2 = models.TextField()
    instagram_seo_link2 = models.TextField()
    instagram_seo_htmlcontent1 = HTMLField()
    instagram_seo_htmlcontent2 = HTMLField()

    canva_header1 = HTMLField()
    canva_header2 = HTMLField()
    canva_header_image = models.ImageField()
    canva_button1 = models.TextField()
    canva_link1 = models.TextField()
    canva_button2 = models.TextField()
    canva_link2 = models.TextField()
    canva_htmlcontent1 = HTMLField()
    canva_htmlcontent2 = HTMLField()

    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return f"FastTrackTrainingPage updated on {self.updated}"
    
    from django.db import models

class Pagelinks(models.Model):
    # Each product's name and URL as separate fields

    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this

    title1 = HTMLField()
    title2 = HTMLField()
    title3 = HTMLField()
    title4 = HTMLField(null=True)

    product1name = HTMLField()
    product1url = models.URLField(max_length=512)
    
    product2name = HTMLField()
    product2url = models.URLField(max_length=512)
    
    product3name = HTMLField()
    product3url = models.URLField(max_length=512)
    
    product4name = HTMLField()
    product4url = models.URLField(max_length=512)
    
    product5name = HTMLField()
    product5url = models.URLField(max_length=512)
    
    product6name = HTMLField()
    product6url = models.URLField(max_length=512)
    
    product7name = HTMLField()
    product7url = models.URLField(max_length=512)
    
    product8name = HTMLField()
    product8url = models.URLField(max_length=512)
    
    product9name = HTMLField()
    product9url = models.URLField(max_length=512)
    
    product10name = models.CharField(max_length=255)
    product10url = models.URLField(max_length=512)
    
    product11name = models.CharField(max_length=255)
    product11url = models.URLField(max_length=512)
    
    product12name = models.CharField(max_length=255)
    product12url = models.URLField(max_length=512)
    
    product13name = models.CharField(max_length=255)
    product13url = models.URLField(max_length=512)
    
    product14name = models.CharField(max_length=255)
    product14url = models.URLField(max_length=512)
    
    product15name = models.CharField(max_length=255)
    product15url = models.URLField(max_length=512)
    
    product16name = models.CharField(max_length=255)
    product16url = models.URLField(max_length=512)
    
    product17name = models.CharField(max_length=255)
    product17url = models.URLField(max_length=512)
    
    product18name = models.CharField(max_length=255)
    product18url = models.URLField(max_length=512)
    
    product19name = models.CharField(max_length=255)
    product19url = models.URLField(max_length=512)
    
    product20name = models.CharField(max_length=255)
    product20url = models.URLField(max_length=512)
    
    product21name = models.CharField(max_length=255)
    product21url = models.URLField(max_length=512)
    
    product22name = models.CharField(max_length=255)
    product22url = models.URLField(max_length=512)
    
    product23name = models.CharField(max_length=255)
    product23url = models.URLField(max_length=512)
    
    product24name = models.CharField(max_length=255)
    product24url = models.URLField(max_length=512)
    
    product25name = models.CharField(max_length=255)
    product25url = models.URLField(max_length=512)
    
    product26name = models.CharField(max_length=255)
    product26url = models.URLField(max_length=512)
    
    product27name = models.CharField(max_length=255)
    product27url = models.URLField(max_length=512)
    
    product28name = models.CharField(max_length=255)
    product28url = models.URLField(max_length=512)
    
    product29name = models.CharField(max_length=255)
    product29url = models.URLField(max_length=512)
    
    product30name = models.CharField(max_length=255)
    product30url = models.URLField(max_length=512)
    
    product31name = models.CharField(max_length=255)
    product31url = models.URLField(max_length=512)

    class Meta:
        ordering = ['-updated']  # corrected 'orderby' to 'ordering'

    def __str__(self):
        return "Product Links"

