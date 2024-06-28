# /apps/api/afbcore/tests/views/test__requests__view.py

from afbcore.models import FoodRequest
from afbcore.views.requests import FoodRequestViewSet
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

User = get_user_model()


class FoodRequestViewSetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            name="Abc",
            email="testuser@example.com",
            password="testpassword",
        )
        cls.factory = APIRequestFactory()
        cls.view = FoodRequestViewSet.as_view({"post": "create"})
        cls.url = "/api/v1/requests/"

    def setUp(self):
        pass

    def test_create_food_request_partial(self):
        data = {
            "title": "New FoodRequest",
            "description": "New Description",
            "user": self.user.id,
        }
        request = self.factory.post(self.url, data, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_food_request(self):
        data = {
            "user": str(self.user.id),
            "address_text": "1234 Southview Drive SE, Medicine Hat, AB, Canada",
            "address_google_place_id": None,
            "address_canadapost_id": None,
            "address_latitude": None,
            "address_longitude": None,
            "contact_name": "Delbo Baggins",
            "contact_phone": "(123) 456-7890",
            "method_of_contact": "Call",
            "delivery_contact": {
                "choose_contact": True,
                "contact_name": "Delbo Baggins",
                "preferred_method": "Call",
                "contact_phone": "(123) 456-7890",
            },
            "pets": {
                "which_pets": "All",
                "pets": [
                    {
                        "pet_type": "Dog",
                        "pet_name": "Frankie",
                        "pet_dob": "2020",
                        "food_details": {
                            "allergies": "Being picked up",
                            "foodtype": "Either",
                        },
                        "dog_details": {"size": "10-20 lbs (Small)"},
                        "spay_or_neutered": "Yes",
                        "general_notes": None,
                    }
                ],
            },
            "confirmation": {"confirm_info": True, "accept_terms": True},
            "safe_drop": {"confirm": True, "instructions": "Side door"},
        }
        request = self.factory.post(self.url, data, format="json")
        force_authenticate(request, user=self.user)

        response = self.view(request)
        print(response.data)  # Add this line to print the response data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
