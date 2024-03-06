from rest_framework import serializers
from food_store.models import Category, SubCategory, Product, Cart


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    def get_subcategories(self, obj):
        subcategories = obj.subcategory_set.all()  # Получаем все связанные подкатегории
        return SubCategorySerializer(subcategories, many=True).data

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'subcategories']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.subcategory.category.name

    def get_subcategory(self, obj):
        return obj.subcategory.name

    def get_images(self, obj):
        images = [obj.image1, obj.image2, obj.image3]
        return [image.url if image else None for image in images]

    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'subcategory', 'price', 'images']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Cart
        fields = ['product_name', 'quantity']
