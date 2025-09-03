# main_app/forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["app_name", "message"]
        widgets = {
            "app_name": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
        }
