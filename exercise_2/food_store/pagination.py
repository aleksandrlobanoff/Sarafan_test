from rest_framework.pagination import PageNumberPagination


# Определение класса пагинации

class CategoryPagination(PageNumberPagination):
    page_size = 10  # Количество категорий на странице
    page_query_param = 'page'  # Параметр для указания номера страницы в URL
    page_size_query_param = 'page_size'  # Параметр для указания количества категорий на странице в URL
    max_page_size = 100  # Максимальное количество категорий на странице


# Определение класса пагинации
class ProductPagination(PageNumberPagination):
    page_size = 10  # Количество элементов на странице
    page_size_query_param = 'page_size'
    max_page_size = 100
