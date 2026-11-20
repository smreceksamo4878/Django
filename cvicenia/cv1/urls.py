from django.urls import path
from . import views 

urlpatterns = [
	path('cv1_index/', views.cv1_index, name = "cv1_index"),
	path('obchod/', views.obchod, name = "obchod"),
	path('body/', views.cv1_body, name = "cv1_body"),
]