# your_app/context_processors.py

from .models import Pagelinks

def pagelinks(request):
    # Fetch all Pagelinks from the database
    return {
        'pagelinks': Pagelinks.objects.first()
    }
