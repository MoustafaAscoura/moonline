from django.urls import path
from . import views
app_name='pages'
urlpatterns = [
       path('',views.app,name='app'),
       path('product_view/',views.product_view,name='product_view'),
       path('product_view1/<str:kind>/',views.kind_view,name='kind_view'),
       path('product_view/<str:pk>/',views.details,name='details'),
       path('product_view/<str:pk>/new',views.form_order,name='form_order'),
       #path('form_order/<str:pk>/new',views.form_order,name='form_order'),


       path('contact',views.contact,name='contact'),
       path('thanks',views.thanks,name='thanks'),







       # path('cart_detail/',views.cart_detail,name='cart_detail'),
       # path('add/<int:product_id>/', views.cart_add,name='cart_add'),
       # path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
]