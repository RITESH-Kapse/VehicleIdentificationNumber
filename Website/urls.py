from django.urls import path
from Website import views
from .import views

urlpatterns = [

	path('', views.Details, name="Details"),
	path('History/', views.History, name="History"),
	path('Results/', views.Results, name="Results"),
	path('index/', views.index, name="index"),

]