from django.contrib import admin
from .models import StudentInfo

class studData(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "name", "email", "mobile", "dob", "address", "gender"]

admin.site.register(StudentInfo, studData)
