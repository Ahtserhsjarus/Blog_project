from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('categories/<category_slug>', views.category, name='category'),
    path('blogs/<blog_slug>', views.blog, name='blog'),
    path('search/', views.search, name='search'),

]
