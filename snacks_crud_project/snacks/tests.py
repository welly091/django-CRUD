from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Snack

class ThingTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="Gross Pie Cookie", description="So Gross", purchaser=self.user
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Gross Pie Cookie")

    def test_thing_content(self):
        self.assertEqual(f"{self.snack.title}", "Gross Pie Cookie")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.description, "So Gross")

    def test_thing_list_view(self):
        response = self.client.get(reverse("SnackListView"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gross Pie Cookie")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_thing_detail_view(self):
        response = self.client.get(reverse("SnackDetailView", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("SnackCreateView"),
            {
                "title": "Fish Cake",
                "description": "Taste like fish. Rusty.",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("SnackDetailView", args="2"))
        self.assertContains(response, "Taste like fish. Rusty")

    def test_thing_update_view_redirect(self):
        response = self.client.post(
            reverse("SnackUpdateView", args="1"),
            {"title": "Updated name", "description": "low on calories", "purchaser": self.user.id}
        )

        self.assertRedirects(response, reverse("SnackDetailView", args="1"))

    def test_thing_delete_view(self):
        response = self.client.get(reverse("SnackDeleteView", args="1"))
        self.assertEqual(response.status_code, 200)