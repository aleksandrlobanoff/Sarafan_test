from django.urls import path
from . import views
from food_store.apps import FoodStoreConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from .views import CartView

app_name = FoodStoreConfig.name

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API for my project",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    # Категория
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', views.CreateCategoryAPIView.as_view(), name='create-category'),
    path('category/edit/<int:id>/', views.EditCategoryAPIView.as_view(), name='edit-category'),
    path('category/delete/<int:pk>/', views.DeleteCategoryAPIView.as_view(), name='delete-category'),
    # Продукты
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.CreateProductView.as_view(), name='create_product'),
    path('products/<slug:slug>/update/', views.UpdateProductView.as_view(), name='update_product'),
    path('products/<slug:slug>/delete/', views.DeleteProductView.as_view(), name='delete_product'),
    # Корзина
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/update/<int:pk>/', views.UpdateCartItemView.as_view(), name='update_cart_item'),
    path('cart/remove/<int:pk>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/summary/', views.CartSummaryView.as_view(), name='cart_summary'),
    # Tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Swaggre/redoc
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
