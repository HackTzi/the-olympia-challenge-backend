"""Customer tests"""

# Django
from django.test import TestCase

# Models
from customers.models import Customer
from django.contrib.auth.models import User


class CustomerTest(TestCase):
    """Test module for Customer Model"""

    def setUp(self):
        user = User.objects.create_user(
            first_name='Elon', last_name='Musk',
            email='ceo@tesla.com', password='S3XY')
        user.save()

        Customer.objects.create(
            user=user, work_area='software_development',
            country='US', phone_number='+1 1250000012',
            currency='USD', points=0)
