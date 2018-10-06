from django.urls import path
from . import views

urlpatterns = [
    path('user_register', views.user_registration, name='user_registration'),
    path('admin_register', views.admin_registration, name='admin_registration'),
    path('code_detail', views.code_detail, name='code_detail'),
    path('code_used_count', views.code_used_count, name='code_used_count')
]