# Generated by Django 3.2 on 2023-09-27 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0004_auto_20230927_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['user'], 'verbose_name': 'Избранный рецепт', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ['user'], 'verbose_name': 'Корзина покупок', 'verbose_name_plural': 'Корзина покупок'},
        ),
        migrations.RemoveConstraint(
            model_name='favorite',
            name='unique_shopping_cart',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ShoppingCart', to='recipes.recipe', verbose_name='Рецепты пользователей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ShoppingCart', to='users.user', verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='favorite',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='recipes.recipe', verbose_name='Рецепты пользователей'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_favourites'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_shopping_cart'),
        ),
    ]
