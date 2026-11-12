from django.urls import path
from . import views 

urlpatterns = [
	path('o-mne/', views.o_mne, name = "o_mne"),
	path('vizitka/', views.du2_, name = "du2_"),
]