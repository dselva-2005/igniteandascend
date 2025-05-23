# your_app/context_processors.py

from .models import Pagelinks, Footer
def pagelinks(request):
    # Fetch all Pagelinks from the database
    return {
        'pagelinks': Pagelinks.objects.first(),
        'footer': Footer.objects.first(),
    }
