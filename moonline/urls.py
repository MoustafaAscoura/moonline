"""
URL configuration for moonline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .views import stripePay,paysuccess
from django.conf import settings

urlpatterns = [
]
urlpatterns +=i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('pages.urls',namespace='pages')),
    path('templates/', stripePay,name="main_home"),
    path('templates/pay_success/', paysuccess, name='Success_page'),






)
# +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG is True:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
