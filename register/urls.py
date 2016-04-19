from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^form_register/', views.form_register, name='form_register'),
]

