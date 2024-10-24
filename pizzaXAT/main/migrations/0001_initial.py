# Generated by Django 5.1.2 on 2024-10-24 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('discription', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('img', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('discription', models.CharField(max_length=100)),
                ('item_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.itemmenu')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField()),
                ('sum', models.FloatField()),
                ('item_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.itemmenu')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=15)),
                ('adress', models.CharField(max_length=50)),
                ('img', models.FilePathField()),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.orders')),
            ],
        ),
    ]
