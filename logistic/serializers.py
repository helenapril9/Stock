from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']
        # настройте сериализатор для продукта

class ProductPositionSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True)
    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'price','quantity']

    # настройте сериализатор для позиции продукта на складе

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id','address','positions']
    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
#        for position in positions:

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        for position in positions:
            product = position['product']
            quantity = position['quantity']
            price = position['price']
            stock = stock ['address ']
            StockProduct.object.create_update(stock=stock, product=product, quantity=quantity, price=price)
        return stock
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions


