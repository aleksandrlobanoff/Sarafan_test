from django.urls import path
from . import views
from food_store.apps import FoodStoreConfig

app_name = FoodStoreConfig.name

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', views.CreateCategoryAPIView.as_view(), name='create-category'),
    path('category/edit/<int:pk>/', views.EditCategoryAPIView.as_view(), name='edit-category'),
    path('category/delete/<int:pk>/', views.DeleteCategoryAPIView.as_view(), name='delete-category'),
]
