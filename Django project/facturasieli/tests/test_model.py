# facturasieli/tests/test_models.py

from django.test import TestCase
from facturasieli.models import Company, Address, Profile

class CompanyModelTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=12,
            street="123 Main Street",
            city="Anytown",
            zip_code="12345",
            country="AnyCountry"
        )
        self.company = Company.objects.create(
            siret="12345678901234",
            name="Test Company",
            address=self.address
        )

    def test_company_creation(self):
        self.assertEqual(self.company.siret, "12345678901234")
        self.assertEqual(self.company.name, "Test Company")
        self.assertEqual(self.company.address, self.address)

    def test_string_representation(self):
        self.assertEqual(str(self.company), "Test Company")
