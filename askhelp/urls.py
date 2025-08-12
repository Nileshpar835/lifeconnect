from django.urls import path
from .import views

urlpatterns=[
   path('',views.help_list,name='help_list'),
   path('new/',views.help_create,name='help_create'),
   path('edit/<int:pk>/',views.help_update,name='help_update'),
   path('delete/<int:pk>/',views.help_delete,name='help_delete')

]