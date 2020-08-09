from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.blog, name='blog-blog'),
    path('notice/', views.notice, name='blog-notice'),
    path('about/', views.about, name='blog-about'),

    path('blogs/<str:id>', views.read_more, name='blog-read_more'),
]
