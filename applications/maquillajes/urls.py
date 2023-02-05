from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import  static

app_name = "mk"
urlpatterns = [
    path('maquillajes/', views.maquillajes.as_view(), name= ' listado1'),
    path('search/', views.search.as_view(), name= 'search')
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)