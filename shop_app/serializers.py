from rest_framework import serializers
from .models import Cart, CartItem, Product

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = ["id", "name", "slug", "image", "description", "category", "price"]

class DetailedProductSerializer(serializers.ModelSerializer):
    similar_products = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id", "name", "price", "slug", "image", "description", "similar_products"]

    def get_similar_products(self, product):
        products = Product.objects.filter(category=product.category).exclude(id=product.id)
        serializer = ProductSerializer(products, many=True)
        return serializer.data
    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = ["id", "cart_code", "created_at", "modified_at"]

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    cart = CartSerializer(read_only=True)
    class Meta:
        model = CartItem
        field = ["id", "quantity", "product", "cart"]
