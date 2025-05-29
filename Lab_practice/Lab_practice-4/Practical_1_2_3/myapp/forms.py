from django import forms
from .models import StudentInfo

class studinfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = "__all__"
