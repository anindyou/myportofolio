from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Service


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            institution="Fasilkom UI",
            started_at = timezone.now().date(),
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.institution, "Fasilkom UI")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}#experience"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("api:experience-list"))

        self.assertEqual(response.data, [])

    def test_experience_page_shows_data(self):
        response = self.client.get(reverse("api:experience-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], self.experience.title)
        self.assertEqual(response.data[0]["description"], self.experience.description)
        self.assertEqual(response.data[0]["institution"], self.experience.institution)
        self.assertIsNone(response.data[0]["ended_at"])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now().date()
        self.experience.save()
        response = self.client.get(reverse("api:experience-list"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertIsNotNone(response.data[0]["ended_at"])

class ServiceTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            title="UI/UX Design",
            description="I design intuitive, user-first interfaces.",
            icon="figma-icon.png",
        )

    def test_service_url_is_accessible(self):
        response = self.client.get(reverse("main:show_service")) 

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "service.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}#services"') # tes balik ke main page di bagian service

    def test_service_model(self):
        self.assertEqual(str(self.service), "UI/UX Design")
        self.assertEqual(self.service.icon, "figma-icon.png")

    def test_service_page_shows_data(self):
        response = self.client.get(reverse("api:service-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], self.service.title)
        self.assertEqual(response.data[0]["description"], self.service.description)
    def test_empty_service_page(self):
        Service.objects.all().delete()
        response = self.client.get(reverse("api:service-list"))

        self.assertEqual(response.data, [])