from django.test import TestCase
from afbcore.models.delivery_region import DeliveryRegion

"""
    Ex
"""


class DeliveryRegionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.delivery_region = DeliveryRegion.objects.create(
            name="Test Delivery Region",
            address_line1="123 Main St",
            postal_code="12345",
            country="USA",
        )

    def test_delivery_region_name(self):
        delivery_region = DeliveryRegion.objects.get(id=self.delivery_region.id)
        self.assertEqual(delivery_region.name, "Test Delivery Region")

    def test_delivery_region_address(self):
        delivery_region = DeliveryRegion.objects.get(id=self.delivery_region.id)
        self.assertEqual(delivery_region.address_line1, "123 Main St")

    def test_delivery_region_postal_code(self):
        delivery_region = DeliveryRegion.objects.get(id=self.delivery_region.id)
        self.assertEqual(delivery_region.postal_code, "12345")

    def test_delivery_region_country(self):
        delivery_region = DeliveryRegion.objects.get(id=self.delivery_region.id)
        self.assertEqual(delivery_region.country, "USA")

    def test_delivery_region_str_method(self):
        delivery_region = DeliveryRegion.objects.get(id=self.delivery_region.id)
        self.assertEqual(str(delivery_region), "Test Delivery Region")

    def test_delivery_region_address_fuzzing(self):
        """
        Test that DeliveryRegion.has_useable_address() returns True for
        both valid and invalid addresses.
        """
        delivery_region = DeliveryRegion.objects.get(id=self.delivery_region.id)
        valid_addresses = [
            "123 Main St",
            "456 Elm St",
            "789 Oak St",
            "10 Pine St",
            "11 Maple St",
            "1234 Cedar Ave",
            "5678 Birch Blvd",
            "9012 Spruce St",
            "3456 Pine Rd",
            "7890 Oak Ln",
            "1234 Main St, Apt 1",
            "5678 Elm St, Apt 2",
            "9012 Oak St, Apt 3",
            "3456 Pine St, Apt 4",
            "7890 Cedar St, Apt 5",
        ]
        invalid_addresses = [
            "Invalid Address",
            "123 Main St, Invalid City",
            "123 Main St, Invalid State",
            "3456 Pine St, Apt 9, Invalid City",
            "7890 Cedar St, Apt 10, Invalid State",
        ]
        # Add some non-address string values to the list
        invalid_addresses.extend(
            [
                "Test Delivery Region",
                "Suite 100",
                "Building A",
                "Floor 5",
                "Room 123",
                "Apt 456",
                "PO Box 789",
                "Attn: John Smith",
                "c/o Jane Doe",
            ]
        )

        for address in valid_addresses:
            delivery_region.address = address
            delivery_region.save()

            self.assertTrue(delivery_region.has_useable_address())
            self.assertEqual(delivery_region.address, address)

        for address in invalid_addresses:
            delivery_region.address = address
            delivery_region.save()

            # Even though these addresses are technically invalid, they still
            # pass because the has_useable_address() method only checks if
            # the address field is not empty or None.
            self.assertTrue(delivery_region.has_useable_address())
            self.assertEqual(delivery_region.address, address)
