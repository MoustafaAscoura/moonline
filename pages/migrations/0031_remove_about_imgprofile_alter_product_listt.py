# Generated by Django 4.2.6 on 2023-11-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_alter_order_type_address_alter_product_listt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='imgprofile',
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('classic', 'عصري(كلاسيكي)'), ('Summer', 'قطع صيفية'), ('winter', 'قطع شتوية'), ('discount', 'خصومات'), ('New', 'جديد'), ('Black', 'أسود'), ('ALHajab', 'ALHajab')], max_length=100, verbose_name='تصنيف المنتج '),
        ),
    ]
