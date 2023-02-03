from django.shortcuts import render
from . import forms
from json import dumps, loads
import requests
 
local_path = 'http://0.0.0.0:8001/predict'
render_path = 'https://api-sba.onrender.com/predict'

def homePageView(request):
    responseForm = forms.PredictionForm(request.POST or None)
    if request.method =="POST" :
        if responseForm.is_valid() :
            data = dumps(responseForm.cleaned_data)
            response = requests.post(render_path, data=data)
            context = {'response' : response.json()['MIS_Status']}
            return render(request, 'forecast.html', context=context)
    context = {'form' : responseForm}
    return render(request, 'home.html', context=context)
        