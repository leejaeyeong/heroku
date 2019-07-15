from django.urls import path
from . import views

# views를 import해서 view 객체로만 사용한다

urlpatterns = [
     path('', views.portfolio, name='portfolio'),
] 
