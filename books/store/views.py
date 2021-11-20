from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from store.serializers import BooksSerialazer

from store.models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerialazer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields =  ['price']
    search_fields = ['name', 'autor_name']
    ordering_fields = ['price', 'autor_name']

