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
    