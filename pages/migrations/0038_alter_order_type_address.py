# Generated by Django 4.2.11 on 2024-03-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0037_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='type_address',
            field=models.CharField(choices=[('Home', 'منزل'), ('Apartment', 'بناية'), ('office', 'مكتب')], max_length=100, verbose_name='مكان التسليم:'),
        ),
    ]
