# Generated by Django 3.2 on 2023-09-24 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230924_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sub', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания подписки')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Автор рецепта')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ('-id',),
            },
        ),
    ]
