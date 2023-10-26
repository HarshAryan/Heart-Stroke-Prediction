from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    
    #API access routes 
    path('predictstroke',views.do_prediction, name="prediction"),
]
