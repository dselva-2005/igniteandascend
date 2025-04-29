from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    cover_page = models.ImageField()
    title = models.CharField(max_length=50)
    book = models.FileField()
    price = models.IntegerField()

    def get_n_pages(n):
        pass

    def __str__(self):
        return f'{self.title}'
    

class BookPage(models.Model):
    header_html = HTMLField()
    header_image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)  # corrected this
    updated = models.DateTimeField(auto_now=True)      # corrected this


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='purchases', on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(default=timezone.now)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.CharField(max_length=50, choices=[('PENDING', 'Pending'), ('SUCCESS', 'Success'), ('FAILED', 'Failed')], default='PENDING')
    payment_mode = models.CharField(max_length=50, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.username} purchased {self.book.name} on {self.purchased_at}"