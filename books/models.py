from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Book(models.Model):
    cover_page = models.ImageField()
    title = models.CharField(max_length=50)
    book = models.FileField()

    def get_n_pages(n):
        pass

    def __str__(self):
        return f'{self.title}'
    

class BookPage(models.Model):
    header_html = HTMLField()
    header_image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this