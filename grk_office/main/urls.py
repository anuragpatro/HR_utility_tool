from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('show_data',views.show_data,name='person'),
    #path('admin/', admin.site.urls),
]
