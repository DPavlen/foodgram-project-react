# Generated by Django 3.2 on 2023-09-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name'], 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='units',
            new_name='measurement_unit',
        ),
        migrations.RenameField(
            model_name='ingredientinrecipe',
            old_name='quantity',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.SmallIntegerField(default=1, help_text='Ввведите время приготовления', verbose_name='Время приготовления блюда'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавте рецепт', upload_to='recipes/images', verbose_name='Изображение рецепта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', to='recipes.IngredientInRecipe', verbose_name='Ингредиенты в рецепте'),
        ),
    ]