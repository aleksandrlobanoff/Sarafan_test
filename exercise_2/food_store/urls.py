from django.urls import path
from . import views
from food_store.apps import FoodStoreConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = FoodStoreConfig.name

urlpatterns = [
    # Категория
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', views.CreateCategoryAPIView.as_view(), name='create-category'),
    path('category/edit/<int:pk>/', views.EditCategoryAPIView.as_view(), name='edit-category'),
    path('category/delete/<int:pk>/', views.DeleteCategoryAPIView.as_view(), name='delete-category'),
    # Продукты
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.CreateProductView.as_view(), name='create_product'),
    path('products/<slug:slug>/update/', views.UpdateProductView.as_view(), name='update_product'),
    path('products/<slug:slug>/delete/', views.DeleteProductView.as_view(), name='delete_product'),
    #Tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
