from django.shortcuts import render
from . import forms
from json import dumps, loads
import requests
 

def homePageView(request):
    responseForm = forms.PredictionForm(request.POST or None)
    if request.method =="POST" :
        if responseForm.is_valid() :
            data = dumps(responseForm.cleaned_data)
            response = requests.post('http://127.0.0.1:8001/predict', data=data)
            context = {'response' : response.text}
            return render(request, 'forecast.html', context=context)
    context = {'form' : responseForm}
    return render(request, 'home.html', context=context)
        