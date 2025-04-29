from django.views.generic import ListView
from books.models import Book
    
class Books(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ebooks"
        return context
    