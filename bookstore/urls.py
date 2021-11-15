from  django.urls import path
from  . import views


urlpatterns = [
    path('', views.home ,  name="home"),
    path('customer/<str:pk>', views.customer ,  name="customer"),
    path('books/', views.books, name="book"),
    path('create/', views.create,  name="create"),
    path('update/<str:pk>', views.update,  name="update"),
    path('delete/<str:pk>', views.delete, name="delete"),
    path('login/', views.login,  name="login"),
    path('register/', views.register, name="register"),

]