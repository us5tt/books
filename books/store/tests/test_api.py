from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from store.models import Book
from store.serializers import BooksSerialazer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='Test book 1', price=25,
                                          autor_name = 'Author 1')
        self.book_2 = Book.objects.create(name='Test book 2', price=55,
                                          autor_name = 'Author 5')
        self.book_3 = Book.objects.create(name='Test book Author 1', price=55,
                                          autor_name = 'Author 2')

    def test_get(self):
        url=reverse('book-list')
#        print(url)
        response = self.client.get(url)
#        print(response)
#        print(response.data)
        serializer_data = BooksSerialazer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BooksSerialazer([self.book_1, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

