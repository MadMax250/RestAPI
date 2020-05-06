from django.contrib import admin

# Register your models here.
from .models import Artical

admin.site.register(Artical)
admin.site.site_header = "Rest Web Service"
admin.site.site_title = "Rest API"