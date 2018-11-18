from rest_framework import serializers
from .models import Food,Food_Category


class Food_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Category
        fields = ('ID', 'Category_Name')


class FoodSerializer(serializers.ModelSerializer):
    Food_Category_ID = Food_Category_Serializer()

    class Meta:
        model = Food
        fields = ('Food_Category_ID', 'Food_ID', 'Food_Name', 'Food_Discount', 'Food_Price', 'Keywords', 'ratings_count', 'Rating')
        read_only_fields = ('ratings_count', 'Rating',)

    def create(self, validated_data):
        Food_Category_ID_data = validated_data.pop('Food_Category_ID')
        Food_Category_ID = Food_Category.objects.create(**Food_Category_ID_data)
        ratings_count = 0
        Rating = 0
        food = Food.objects.create(Food_Category_ID=Food_Category_ID, ratings_count=ratings_count, Rating=Rating , **validated_data)
        return food

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        print(validated_data)
        instance.Food_Price = validated_data.get('Food_Price')
        instance.Food_Name = validated_data.get('Food_Name')
        instance.Food_Discount = validated_data.get('Food_Discount')
        instance.save()
        return instance