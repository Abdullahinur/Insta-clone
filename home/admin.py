from django.contrib import admin
from .models import Profile, Image


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('Meta',)


admin.site.register(Profile)
admin.site.register(Image)
