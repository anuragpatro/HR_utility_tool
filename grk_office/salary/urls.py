from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_salary,name='home'),
    path('show_salary',views.show_salary,name = 'salary'),
    path('monthly',views.monthly,name = 'monthly')
]
