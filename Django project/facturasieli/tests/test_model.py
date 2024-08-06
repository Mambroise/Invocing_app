# facturasieli/tests/test_models.py

from django.test import TestCase
from django.utils import timezone

from facturasieli.models import Company, Address, Invoice, VAT_choice


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

class InvoiceModelTest(TestCase):

    def setUp(self):

        self.provider_address = Address.objects.create(
            number = 12,
            street="123 Main Street",
            addings="123 Main building",
            city="Anytown",
            zip_code="12345",
            country="AnyCountry"
        )

        self.client_address = Address.objects.create(
            number = 13,
            street=" murdeer Street",
            addings="123 soleil",
            city="Anycity",
            zip_code="12865",
            country="AnyState"
        )

        self.invoice = Invoice.objects.create(
            invoice_number = 321654,
            issue_date = timezone.now().date(),
            due_date = timezone.now().date() + timezone.timedelta(days=30),
            kind_of_payment = "Bank transfer",
            name_provider = "provider name",
            name_client = "client name",
            hours = 10.5,
            amount_excluding_tax = 100.50,
            tax = 1,
            status = 1,
            client_address = self.client_address,
            provider_address = self.provider_address,
            update_timestamp = timezone.now()
        )
    def test_invoice_creation(self):
        self.assertEqual(self.invoice.invoice_number, 321654)
        self.assertEqual(self.invoice.name_provider, "provider name")
        self.assertEqual(self.invoice.name_client, "client name")
        self.assertEqual(self.invoice.hours, 10.5)
        self.assertEqual(self.invoice.amount_excluding_tax, 100.50)
        self.assertEqual(self.invoice.tax, 1)
        self.assertEqual(self.invoice.status, 1) 
        self.assertEqual(self.invoice.client_address, self.client_address) 
        self.assertEqual(self.invoice.provider_address, self.provider_address) 

    def test_due_date(self):
        # Verify that due_date is correctly set to 30 days after issue_date
        self.assertEqual(self.invoice.due_date, self.invoice.issue_date + timezone.timedelta(days=30))