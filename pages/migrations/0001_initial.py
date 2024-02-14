# Generated by Django 4.2.6 on 2023-11-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='Name')),
                ('product_description', models.TextField(verbose_name=' Description')),
                ('product_image', models.ImageField(default='products/product.jpg', max_length=500, upload_to='products/imgs/', verbose_name='Product Image')),
                ('PRDPrice', models.FloatField(blank=True, null=True, verbose_name='Price')),
                ('PRDDiscountPrice', models.FloatField(blank=True, default=0, null=True, verbose_name='Discount')),
                ('additional_image_1', models.ImageField(blank=True, max_length=500, null=True, upload_to='products/imgs/product_imgs/', verbose_name='Additional  Image_1')),
                ('additional_image_2', models.ImageField(blank=True, max_length=500, null=True, upload_to='products/imgs/product_imgs/', verbose_name='Additional  Image_2')),
                ('additional_image_3', models.ImageField(blank=True, max_length=500, null=True, upload_to='products/imgs/product_imgs/', verbose_name='Additional  Image_3')),
            ],
        ),
    ]
