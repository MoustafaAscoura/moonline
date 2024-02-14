# Generated by Django 4.2.6 on 2023-11-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_order_phone_alter_order_type_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Note',
            field=models.TextField(null=True, verbose_name=' Note'),
        ),
        migrations.AlterField(
            model_name='order',
            name='width',
            field=models.IntegerField(verbose_name='Abaya Chest'),
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('sold', 'sold'), ('winter', 'winter'), ('ALHajab', 'ALHajab'), ('Summer', 'Summer'), ('New', 'New'), ('Black', 'Black'), ('classic', 'classic')], max_length=100, verbose_name='list:'),
        ),
    ]
