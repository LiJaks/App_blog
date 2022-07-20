from django import forms
from app_blog.models import UploadRecord


class BlogRecordForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, min_length=5, max_length=5000)
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        fields = '__all__'

class UploadRecordForm(forms.ModelForm):
    class Meta:
        model = UploadRecord
        fields = '__all__'
