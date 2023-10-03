from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
#from djoser.serializers import SetPasswordSerializer
from drf_extra_fields.fields import Base64ImageField


from recipes.models import (
    Ingredient, Tag, Recipe, IngredientInRecipe, Favorite, ShoppingCart)
from users.models import User, Subscriptions


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания переопределенного Usera и
    проверки просмотра подписок."""
    is_subscribed = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'password',
        )
        # поле "password" будет доступно только для записи 
        extra_kwargs = {'password': {'write_only': True}}
                        

    def create(self, validated_data):
        """Создание нового пользователя с указанными полями."""
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
    def get_is_subscribed(self, author):
        """Проверка подписки пользователей. Определяет - подписан ли текущий пользователь
        на просматриваемого пользователя(True or False)."""
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return Subscriptions.objects.filter(user=user, author=author).exists()


class UserSubscriptionsSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок пользователя. 
    Выводится текущий пользователь."""
    recipes_count = SerializerMethodField()
    recipes = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'recipes',
            'recipes_count',
        )


    def get_recipes(self, author):
        """Количество рецептов, связанных с текущим автором."""
        return author.recipes.count()
    

    def get_recipes_count(self, author):
        """Получить количество рецептов для данного автора."""
        request = self.context.get('request')
        limit = request.GET.get('recipes_limit')
        recipes = author.recipes.all()[:int(limit)] if limit else author.recipes.all()
        serializer = ShortRecipeSerializer(recipes, many=True, read_only= True)
        return serializer.data
    
    def validate(self, data):
        """Проверка на повторную подписку к существующему пользователю.
        Проверка на подписку самого себя."""
        author = self.instance
        user = self.context.get('request').user
        if Subscriptions.objects.filter(author=author, user=user).exists():
            raise ValidationError(
                'Вы уже подписаны на этого пользователя себя!'
                )
        if user == author:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return data
    


class ShortRecipeSerializer(serializers.ModelSerializer):
    """Сериализатор короткого рецепта.
    image позволяет передавать изображения в виде base64-строки по API."""
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'image',
            'cooking_time',
        )


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор для получения Тегов."""
    class Meta:
        model = Tag
        fields = (
            'id',
            'name', 
            'slug',
            'color',
        )      


class IngredientSerializer(serializers.ModelSerializer):
    """Сериализатор для получения Ингредиентов."""
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name', 
            'measurement_unit',
        )      
