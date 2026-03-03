from django.urls import path
from .views import emp_add,emp_list,emp_edit,emp_delete,emp_bulk_delete

urlpatterns=[
    path('',emp_add,name='emp_add'),
    path('list/',emp_list,name='emp_list'),
    path('edit/<int:id>/',emp_edit,name='emp_edit'),
    path('delete/<int:id>/',emp_delete,name='emp_delete'),
    path('bulk-delete/', emp_bulk_delete,name='emp_bulk_delete'),
]