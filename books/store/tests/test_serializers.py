from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerialazer


class BookSerializerTestCase(TestCase):
    def test_ok(selfself):
        book_1 = Book.objects.create(name='Test book 1', price=25)
        book_2 = Book.objects.create(name='Test book 2', price=55)
        data = BooksSerialazer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '55.00',
            },

        ]
 #       self.assertEqual(expected_data, data)


