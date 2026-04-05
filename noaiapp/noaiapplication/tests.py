from django.test import TestCase
from .models import Person

class PersonTestCases(TestCase):
    def setUp(self):
        self.p = Person.objects.create(name='subba reddy', shirt_size='M')
        self.p1=Person.objects.create(name='Arikatle', shirt_Size='L')

    def test_person_created(self):
        self.assertEqual(self.p.name, 'subba reddy')
        self.assertEqual(self.p.shirt_size, 'M')
        self.assertEqual(self.p1.name, 'Arikatla')
        self.assertEqual(self.p1.shirt_size, 'L')

@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    if created:
        print("created")
    else:
        print("updated")

class ProductTest(TestCase):
    def test_api(self):
        self.assertEqual(200, 404)
