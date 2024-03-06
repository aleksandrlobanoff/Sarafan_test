from rest_framework.pagination import PageNumberPagination


# Определение класса пагинации
class CategoryPagination(PageNumberPagination):
    page_size = 10  # Количество элементов на странице
    page_size_query_param = 'page_size'
    max_page_size = 100

