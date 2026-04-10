from django.test import TestCase
from .models import Person
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student, Professional


class StudentAPITest(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name='Subba Reddy',
            email='subba@example.com',
            grade='10',
            age=20
        )

    def test_get_students(self):
        response = self.client.get(reverse('student-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        data = {
            'name': 'Ravi',
            'email': 'ravi@example.com',
            'grade': '9',
            'age': 18
        }
        response = self.client.post(reverse('student-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_student(self):
        data = {
            'name': 'Updated Name',
            'email': 'subba@example.com',
            'grade': '11',
            'age': 21
        }
        response = self.client.put(reverse('student-detail', args=[self.student.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self):
        response = self.client.delete(reverse('student-detail', args=[self.student.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProfessionalAPITest(APITestCase):
    def setUp(self):
        self.professional = Professional.objects.create(
            name='Anil Kumar',
            email='anil@example.com',
            role='Trainer',
            company='ABC Institute'
        )

    def test_get_professionals(self):
        response = self.client.get(reverse('professional-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_professional(self):
        data = {
            'name': 'Meena',
            'email': 'meena@example.com',
            'role': 'Developer',
            'company': 'XYZ Tech'
        }
        response = self.client.post(reverse('professional-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_professional(self):
        data = {
            'name': 'Updated Professional',
            'email': 'anil@example.com',
            'role': 'Senior Trainer',
            'company': 'ABC Institute'
        }
        response = self.client.put(reverse('professional-detail', args=[self.professional.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_professional(self):
        response = self.client.delete(reverse('professional-detail', args=[self.professional.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)