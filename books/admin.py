from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.BookPage)