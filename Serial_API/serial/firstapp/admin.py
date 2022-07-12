from django.contrib import admin

# Register your models here.

from .models import Genre
from .models import Serial
from .models import Image
from .models import Cast

admin.site.register(Genre)
admin.site.register(Serial)
admin.site.register(Image)
admin.site.register(Cast)