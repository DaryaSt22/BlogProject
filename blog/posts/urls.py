from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_post),
    path('',views.index_html),
    path("about/", views.about),
    path('go/<int:posts>/', views.my_new_url),
    path('home/', views.index),
]
