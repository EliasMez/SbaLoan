from django.shortcuts import render
from . import forms
from json import dumps, loads
import requests
 
local_path = 'http://0.0.0.0:8001/predict'
# render_path = 

def homePageView(request):
    responseForm = forms.PredictionForm(request.POST or None)
    if request.method =="POST" :
        if responseForm.is_valid() :
            data = dumps(responseForm.cleaned_data)
            response = requests.post(local_path, data=data)
            context = {'response' : response.text}
            return render(request, 'forecast.html', context=context)
    context = {'form' : responseForm}
    return render(request, 'home.html', context=context)
        