from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.app, name='app'),
    path('product_view/<str:pk>/', views.details, name='details'),
    path('product_view/<str:pk>/new', views.form_order, name='form_order'),
    path('product_view1/<str:kind>/', views.kind_view, name='kind_view'),
    path('contact', views.contact, name='contact'),
    path('thanks', views.thanks, name='thanks'),
]
