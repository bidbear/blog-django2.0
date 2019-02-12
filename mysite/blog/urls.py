from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('', views.blog_list,name='blog_list'),
    path('<int:blog_id>',views.blog_details,name ='blog_details'),
    path('type/<int:blog_type_id>',views.blog_type,name='blog_type'),
]
