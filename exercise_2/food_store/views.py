from rest_framework import generics
from .models import Category
from food_store.serializers import CategorySerializer

from .pagination import CategoryPagination


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination  # Использование класса пагинации для разбивки списка категорий на страницы


class CreateCategoryAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EditCategoryAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'  # Поле для поиска существующей категории по идентификатору


class DeleteCategoryAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'  # Поле для поиска существующей категории по идентификатору
