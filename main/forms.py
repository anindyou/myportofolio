from django.forms import ModelForm, TextInput, Textarea, DateInput

from main.models import Service, Experience
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = [
            "title",
            "description",
            "icon",
        ]

        labels = {
            "title": "Service name",
            "description": "Service description",
            "icon": "Icon path",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Service name",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your service",
                    "rows": 3,
                }
            ),
            "icon": TextInput(
                        attrs={
                            "placeholder": "xx-xx.png",
                            "maxlength": 255,
                        }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Service name can't be an HTML tag")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_icon(self):
            return strip_tags(self.cleaned_data["icon"]).strip()
    
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "institution",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Experience name",
            "description": "Experience description",
            "institution": "Place",
            "started_at": "Start date",
            "ended_at": "End date",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Experience name",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your experience",
                    "rows": 3,
                }
            ),
            "institution": TextInput(
                        attrs={
                            "placeholder": "Who accomodate this idk",
                            "maxlength": 255,
                        }
            ),
            "started_at": DateInput(
                        attrs={
                            "type": "date",
                        }
            ),
            "ended_at": DateInput(
                        attrs={
                            "type": "date",
                        }
            ),
        }