from django.contrib import admin
from django.utils.html import format_html
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('id', 'name', 'specialty', 'phone_number', 'email', 'display_image' , 'discription', 'fees')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:50%;" />', obj.image.url)
        return "No Image"

    display_image.short_description = 'Profile Image'

admin.site.register(Doctor, DoctorAdmin)
