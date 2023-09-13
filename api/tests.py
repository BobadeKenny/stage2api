from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status

from api.models import Person

class PersonTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.person = Person.objects.create(name='John Doe')

    def test_create_person(self):
        url = reverse('person-list')
        data = {'name': 'Jane Doe'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(Person.objects.get(name='Jane Doe').name, 'Jane Doe')
        self.assertEqual(response.data['message'], 'Person created')

    def test_update_person(self):
        url = reverse('person-detail', args=[self.person.id])
        data = {'name': 'Julie Doe'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get(name='Julie Doe').name, 'Julie Doe')
        self.assertEqual(response.data['message'], 'Person Julie Doe updated')

    def test_delete_person(self):
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 0)
        self.assertEqual(response.data['message'], 'John Doe deleted')

    def test_retrieve_person(self):
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')
