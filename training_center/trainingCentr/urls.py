"""trainingCentr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from Centr import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:object_id>', views.detailed, name='detailed'),
    path('info_program/<str:title>', views.info_program, name='info_program'),  #  /<int:program_id>/
    path('admin/', admin.site.urls),
    path('/', admin.site.urls),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('record_view', views.record_view, name='record_view'),
    path('callback', views.callback_form, name='callback_form'),
    path('payment', views.payment_form, name='payment_form'),
    path('info_program/payment_form/', views.payment_form, name='payment_form'),
    path('prerpodg', views.prerpodg_view, name='prerpodg'),
    path('dopodgot', views.dopodgot_view, name='dopodgot'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
