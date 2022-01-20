from unicodedata import name
from django.urls import path
from registerData import views

urlpatterns = [
    path('',views.index,name='User Form'),
    path('show/',views.show,name='Show Users'),
    path('edit/<int:id>',views.edit,name='Edit User'),
    path('update/<int:id>',views.update,name='Update User'),
    path('delete/<int:id>',views.destroy,name='Delete User'),
    ]