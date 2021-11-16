from .apps import AppConfig
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np
import pandas as pd

# Create your views here.
class AdherencePrediction(APIView):
  def post(self,requests):
    data = requests.data
    age = data['age']
    prefix = data['prefix'] #mr=0,mrs=1,ms=2,master=3
    maritial = data['maritial'] #M=1,S=0
    gender = data['gender']#m=1,f=0
    lat =  data['lat']
    long =  data['lon']
    HealthCareExp = data['HealthCareExpense'] #in lakhs decimals
    model = AppConfig.model
    predicted = model.predict([[age,prefix,maritial,gender,lat,long,HealthCareExp]])
    response_dict = {"Adherence": predicted}
    return Response(response_dict, status=200)