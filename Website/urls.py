from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.Details, name="Details"),
	path('History/', views.History, name="History"),
	path('Results/', views.Results, name="Results"),

]