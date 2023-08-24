from django.urls import path
from myapp import views

urlpatterns = [
    
    
    path('', views.index, name = "index"),
    path('register', views.register, name = "register"),
    path('regbutton', views.regbutton, name = "regbutton"),
    path('savevalue', views.savevalue, name='savevalue'),
    path('observations', views.observations, name='observations'),
    path('consult', views.consult, name='consult'),
    path('proceed', views.consult, name='proceed'),
    path('proceed/<int:record_id>/', views.proceed, name='proceed'),

]
