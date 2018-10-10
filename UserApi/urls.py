from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('user_register', views.user_register, name='user_register'),
    path('', views.login, name='login'),
    path('admin_register', views.admin_register, name='admin_register'),
    path('dashboard/user_type/code_view', views.code_view, name='code_view'),
    url(r'^dashboard/(?P<user_type>\w+?)/$', views.dashboard, name='dashboard'),
    path('code_used_count', views.code_used_count, name='code_used_count'),
    path('dashboard/user_type/generate_csv', views.generate_csv, name='generate_csv')
]