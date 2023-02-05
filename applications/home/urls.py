from django.urls import path

from applications.home import views
urlpatterns = [


path('',views.inicio.as_view(), name='inicio')




    
]