from django.core.files.storage import FileSystemStorage

class ProtectedMediaStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        super().__init__(location='/home/dselva/python_projects/professional_order_1/protected',
                         base_url='/books/secure-media/',  # dummy URL, real serving is via X-Accel-Redirect
                         *args, **kwargs)
