from django.urls import path,re_path
from . import  views
from django.conf.urls import url

app_name = 'my_app'
urlpatterns = [
    path('home/',  views.home, name='主页'),
    re_path(r'^about/$', views.about, name='关于'),
    path('search/', views.search, name='搜索'),
    path('edit/<activity_id>', views.edit, name='编辑'),
    path('delete/<activity_id>/', views.delete, name='删除'),
]
