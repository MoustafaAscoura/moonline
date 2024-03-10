from django.db import models

from django.utils.translation import gettext_lazy as _

from django.db import models
# from categories.models import SubCategory, MainCategory, SuperCategory, MiniCategory
# from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
# from .utils import code_generator, create_shortcode
from django.db.models.signals import pre_save

from django.utils.safestring import mark_safe
from django.core import validators
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from io import BytesIO
# from PIL import Image
from django.core.files import File


class about(models.Model):
    info = models.TextField(_("وصف الخدمات "))
    class Meta:
        verbose_name = _("معلومات الصفحة الرئيسية")
        verbose_name_plural = _("معلومات الصفحة الرئيسية")


class Product(models.Model):
    listt = {('Summer', 'قطع صيفية'),
             ('winter', 'قطع شتوية'),
             ('New', 'جديد'),
             ('classic', 'عصري(كلاسيكي)'),
             ('Black', 'أسود'),
             ('ALHajab', 'ALHajab'),
             ('discount', 'خصومات')
             }

    id = models.IntegerField(primary_key=True, default=True)
    product_name = models.CharField(max_length=150, verbose_name=_("اسم المنتج"), null=False)
    product_description = models.TextField(verbose_name=_(" مواصفات المنتج"))
    listt = models.CharField(_("تصنيف المنتج "), choices=listt, max_length=100)
    product_image = models.ImageField(
        upload_to='products/imgs/', default='products/product.jpg', max_length=500,
        verbose_name=_("صورة رئيسية للمنتج"), null=False)

    PRDPrice = models.FloatField(
        blank=True, verbose_name=_("سعر المنتج"), null=False)

    PRDDiscountPrice = models.FloatField(default=0,
                                         blank=True, null=True, verbose_name=_("خصم على هذه القطعة"))

    additional_image_1 = models.ImageField(
        upload_to='products/imgs/product_imgs/', blank=True, null=True, max_length=500,
        verbose_name=_("صورة2 لنفس المنتج"), )

    additional_image_2 = models.ImageField(
        upload_to='products/imgs/product_imgs/', blank=True, null=True, max_length=500,
        verbose_name=_("صورة 3 لنفس المنتج"), )

    # url = models.URLField()

    class Meta:
        verbose_name = _("المنتجات")
        verbose_name_plural = _("المنتجات")

    def __str__(self):
        return self.product_name


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    name_prod = models.ForeignKey("Product", verbose_name=_("اسم القطعة المطلوبة"), on_delete=models.CASCADE)
    name_customer = models.CharField(null=False, verbose_name=_("اسم الزبون"), max_length=500)

    notes = models.TextField(verbose_name=_(" ملاحظات"), null=True)
    Phone = models.CharField(_("رقم جوال"), max_length=500)
    length = models.IntegerField(_("طول العباية"))
    shoulders = models.IntegerField(_("أكتاف العباية"))
    sleeve = models.IntegerField(_("أكمام العباية "))
    width = models.IntegerField(_("صدر العباية"))
    address_types = {('Home', 'منزل'),
             ('Apartment', 'بناية'),
             ('office', 'مكتب'),

             }
    area = models.CharField(_("المنطقة"), max_length=500)
    type_address = models.CharField(_("مكان التسليم:"), choices=address_types, max_length=100)
    block = models.CharField(_("الطابق"), max_length=500)
    street = models.CharField(_("الشارع"), max_length=500)
    house = models.CharField(_("المنزل"), max_length=500)
    district = models.CharField(_("جادة"), max_length=500, default="")
    piece = models.CharField(_("قطعة"), max_length=500, default="")

    # payment=models.BooleanField(_("payment"),default=False)
    amount = models.IntegerField(_("السعر المدفوع"))

    # Slug = models.SlugField(max_length=150, blank=True, null=True, allow_unicode=True, unique=True, verbose_name=_("Slugfiy"))

    class Meta:
        verbose_name = _("الطلبات")
        verbose_name_plural = _("الطلبات")

    def __str__(self):
        return self.name_customer
