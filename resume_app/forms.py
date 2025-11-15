from django import forms
from .models import UploadFile

from django import forms
from .models import UploadFile

class ResumeForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file']

