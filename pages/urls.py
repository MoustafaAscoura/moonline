from django.urls import path
from .views import *

app_name = 'pages'
urlpatterns = [
    path('', app, name='app'),
    path('categories', CategoryListView.as_view(), name='categories' ),
    path('categories/<int:pk>', CategoryView.as_view(), name='category' ),
    path('product/<str:pk>/', details, name='details'),
    path('product/<str:pk>/new', form_order, name='form_order'),
    path('contact', contact, name='contact'),
    path('thanks', thanks, name='thanks'),
]
