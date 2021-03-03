from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('activity.html',views.qp, name='qp'),
    

    

]