# Generated by Django 5.1.2 on 2024-10-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_category_products_menu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default=1, upload_to='static/images/'),
            preserve_default=False,
        ),
    ]
