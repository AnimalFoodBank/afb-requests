import pytest
from afbcore.models import Branch
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

"""
 How to run the tests:
     - pnpm django:test apps/api/afbcore/tests/views/test_branch_viewset.py
"""


class TestBranchViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@afb.pet", name="testuser"
        )
        self.client.force_authenticate(user=self.user)

        self.branch = Branch.objects.create(
            display_name="Test Branch", hidden=False
        )
        self.hidden_branch = Branch.objects.create(
            display_name="Hidden Branch", hidden=True
        )
        self.list_url = reverse("branch-list", kwargs={"version": "v1"})
        self.detail_url = reverse(
            "branch-detail", kwargs={"version": "v1", "pk": self.branch.pk}
        )

    def test_retrieve_list_of_branches_with_default_filters(self):
        response = self.client.get(self.list_url)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response data contains the expected keys
        expected_keys = ["count", "next", "previous", "results"]
        for key in expected_keys:
            self.assertIn(
                key, response.data, f"'{key}' is missing from response data"
            )

        # Assert that 'results' contains the expected number of items
        self.assertEqual(
            len(response.data["results"]), 1
        )  # Only non-hidden branch should be returned

        # Assert that the first item in 'results' has the correct display_name
        self.assertEqual(
            response.data["results"][0]["display_name"], "Test Branch"
        )

        # Optionally, you can add more specific assertions about 'count', 'next', and 'previous'
        self.assertEqual(response.data["count"], 1)
        self.assertIsNone(response.data["next"])
        self.assertIsNone(response.data["previous"])

    def test_retrieve_nonexistent_branch(self):
        nonexistent_url = reverse(
            "branch-detail", kwargs={"version": "v1", "pk": 9999}
        )
        response = self.client.get(nonexistent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
