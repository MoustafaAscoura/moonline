from django import forms
from django.contrib.auth.models import User
from .models import Order
from django.utils.translation import gettext_lazy as _


class Orderform(forms.ModelForm):
        class Meta:
                model = Order
                fields ='__all__'       

# PROUDUCT_QUANTITY_CHOIES=[(i,str(i)) for i in range(1,21)]
# class CartAddProductFrom(forms.Form):
#         quantity =forms.TypedChoiceField(choices=PROUDUCT_QUANTITY_CHOIES,coerce=int)
#         override_quantity=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput) 
#         class Meta:
#                 model = Order
#                 fields =['__all__','quantity','override_quantity']                 