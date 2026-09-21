from django.forms import ModelForm, TextInput, Textarea, DateInput

from main.models import Service, Experience

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