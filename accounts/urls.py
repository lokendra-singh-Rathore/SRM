from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('view_profile/<str:pk_test>/', views.view_profile, name="view_profile"),

    path('add_class/', views.add_class, name="add_class"),
    path('add_fee/', views.Add_fee, name="add_fee"),
    path('update_class/<str:pk>/', views.updateclass, name="update_class"),
    path('delete_order/<str:pk>/', views.deleteorder, name="delete_order"),
    path('add_student/',views.add_student,name='add_student'),
    path('view_fee/',views.View_fee,name='view_fee'),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
    path('view_student/<str:pk>/',views.view_student,name="view_student"),
    
    path('user/',views.user,name="user"),
    path('bookdemo/',views.bookdemo,name="bookdemo"),
    path('contact/',views.contact,name='contact')


]