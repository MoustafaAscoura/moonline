# Generated by Django 4.2.6 on 2023-11-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_rename_note_order_notes_alter_order_type_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
        migrations.AlterField(
            model_name='order',
            name='type_address',
            field=models.CharField(choices=[('Home', 'منزل'), ('office', 'مكتب'), ('Apartment', 'بناية')], max_length=100, verbose_name='مكان التسليم:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('New', 'جديد'), ('Summer', 'قطع صيفية'), ('discount', 'خصومات'), ('winter', 'قطع شتوية'), ('classic', 'عصري(كلاسيكي)'), ('ALHajab', 'ALHajab'), ('Black', 'أسود')], max_length=100, verbose_name='تصنيف المنتج '),
        ),
    ]
