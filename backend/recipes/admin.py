from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from recipes.models import (
    Ingredient,
    Tag,
    Recipe,
    CompositionOfDish,
    Favorite,
    ShoppingCart,
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Настроенная админ-панель Тегов."""

    list_display = (
        "id",
        "name",
        "color",
        "slug",
    )
    search_fields = ("name",)
    list_filter = ("id", "name", "color")


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Настроенная админ-панель Рецептов."""

    list_display = (
        "id",
        "author",
        "name",
        "image",
        "text",
        "cooking_time",
        "pub_date",
    )
    search_fields = ("author",)
    list_filter = (
        "author",
        "name",
        "tags",
    )


@admin.register(CompositionOfDish)
class CompositionOfDishAdmin(admin.ModelAdmin):
    """Настроенная админ-панель Состав блюда."""

    list_display = (
        "id",
        "recipe",
        "ingredient",
        "amount",
    )
    search_fields = ("ingredient",)
    list_filter = ("recipe", "ingredient", "amount")


class IngredientAdmin(resources.ModelResource):
    """Настроенная админ-панель ингредиентов.
    Возможность сделать import и export файлов csv,json."""

    class Meta:
        model = Ingredient
        fields = (
            "id",
            "ingredient",
            "amount",
        )


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    resource_classes = [IngredientAdmin]
    list_filter = ("name",)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Настроенная админ-панель избранные рецепты у пользователей."""

    list_display = ("user", "recipe")
    list_filter = ("user", "recipe")
    search_fields = ("user", "recipe")


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Настроенная админ-панель корзин покупок у пользователей."""

    list_display = ("recipe", "user")
    list_filter = ("recipe", "user")
    search_fields = ("user",)


class CompositionOfDish(admin.TabularInline):
    """Отображение состава блюда в виде таблицы.
    Промежуточная моделт Рецепты, минимум с 1-й строкой."""
    model = CompositionOfDish
    extra = 1
    min_num = 1


class TagRecipeInline(admin.TabularInline):
    """Отображение тегов в виде таблицы.
    Промежуточная моделт Рецепты, минимум с 1-й строкой."""

    model = Recipe.tags.through
    min_num = 1
