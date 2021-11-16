from django.urls import path
from .views import AdherencePrediction

urlpatterns = [
    path('predict/',AdherencePrediction.as_view(), name = 'adherence_prediction'),
]