from django.urls import path
from app import views
urlpatterns = [
    path('employee/',views.employeeView,name='insert'),
    path('empview/<int:vid>/',views.viewemp,name='view'),
    path('empupdate/<int:uid>/',views.empupdate,name='update'),
    path('details/',views.empdetails, name= 'details'),
    path('delete/<int:did>/',views.empdelete, name='delete'), 
]