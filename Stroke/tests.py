from django.urls import path

from . import view

urlpatterns = [
    path('predict_stroke',view.predict, name="predict"),
]
