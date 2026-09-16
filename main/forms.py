from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Service

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
                    "placeholder": "Portfolio Website",
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
                            "placeholder": "ga-tau.png",
                            "maxlength": 255,
                        }
            ),
        }