from django.urls import path,include
from monthlych import views


urlpatterns = [
    path("",views.home,name='home'),
    path("reg",views.regis,name='register'),
    
]
