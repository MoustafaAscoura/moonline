# Generated by Django 4.2.11 on 2024-03-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_alter_order_type_address_alter_product_listt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='type_address',
            field=models.CharField(choices=[('office', 'مكتب'), ('Apartment', 'بناية'), ('Home', 'منزل')], max_length=100, verbose_name='مكان التسليم:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('plain', 'سادة'), ('full', 'ملافع'), ('blazer', 'بليزر'), ('occasion', 'مناسبات')], max_length=100, verbose_name='تصنيف المنتج '),
        ),
    ]