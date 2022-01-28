from django.urls import path
from rango import views 

app_name = 'rango'

urlpatterns = [
# chapter 3
	path('about/', views.about, name='about'),
	path('', views.index, name='index'),
]