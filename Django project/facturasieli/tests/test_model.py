# facturasieli/tests/test_models.py

from django.test import TestCase
from facturasieli.models import Company, Address


class AddressAndCompanyModelTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=12,
            street="123 Main Street",
            addings="123 Main building",
            city="Anytown",
            zip_code="12345",
            country="AnyCountry"
        )
        self.company = Company.objects.create(
            siret="12345678901234",
            name="Test Company",
            address=self.address
        )
    # Address checking
    def test_address_creation(self):
        self.assertEqual(self.address.number, 12)
        self.assertEqual(self.address.street, "123 Main Street")
        self.assertEqual(self.address.addings, "123 Main building")
        self.assertEqual(self.address.city, "Anytown")
        self.assertEqual(self.address.zip_code, "12345")
        self.assertEqual(self.address.country, "AnyCountry")
        

    # Company checking
    def test_company_creation(self):
        self.assertEqual(self.company.siret, "12345678901234")
        self.assertEqual(self.company.name, "Test Company")
        self.assertEqual(self.company.address, self.address)

    def test_string_representation(self):
        self.assertEqual(str(self.company), "Test Company")
