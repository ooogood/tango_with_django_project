from django.urls import path
from rango import views 

app_name = 'rango'

urlpatterns = [
# chapter 3
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
# chapter 6
	path('category/<slug:category_name_slug>/',
		views.show_category, name='show_category'),
# chapter 7
	path('add_category/', views.add_category, name='add_category'),
	path('category/<slug:category_name_slug>/add_page/', 
		views.add_page, name='add_page'),
]