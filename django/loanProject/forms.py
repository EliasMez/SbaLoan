from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
import pickle as pkl
import datetime

# Ouverture d'une liste 
with open('NAICS_list.pkl', 'rb') as fichier:
    depickler = pkl.Unpickler(fichier)
    NAICS_list = depickler.load()

with open('state_list.pkl', 'rb') as fichier:
    depickler = pkl.Unpickler(fichier)
    state_list = depickler.load()

# # DEBUT A SUPPRIMER
# NAICS_list = [('New', 'New Business'), ('Existing', 'Existing Business')]
# state_list = [('New', 'New Business'), ('Existing', 'Existing Business')]
# # FIN A SUPPRIMER

class PredictionForm(forms.Form):

    State = forms.ChoiceField(choices=state_list, initial='NY')
    BankState = forms.ChoiceField(choices=state_list, initial='NY')

    NAICS = forms.ChoiceField(
        choices=NAICS_list,
        initial = '11'
    )

    newExistCHOICES = [('New', 'New Business'), ('Existing', 'Existing Business')]
    NewExist = forms.ChoiceField(choices=newExistCHOICES, widget=forms.RadioSelect, initial='Existing')

    Term = forms.IntegerField(
        initial = 150,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )

    CreateJob = forms.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20000)
        ],
        initial = 10
    )

    urbanRuralCHOICES = [('Undefined', 'Undefined'), ('Urban', 'Urban'), ('Rural', 'Rural')]
    UrbanRural = forms.ChoiceField(choices=urbanRuralCHOICES, widget=forms.RadioSelect, initial='Urban')

    GrAppv = forms.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000000)
        ],
        initial = 10000
    )

    franchiseCHOICES = [('With', 'With'), ('Without', 'Without')]
    Franchise = forms.ChoiceField(choices=franchiseCHOICES, widget=forms.RadioSelect, initial='Without')

    RetainedJob = forms.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20000)
        ],
        initial = 10
    )

    ApprovalFY = forms.IntegerField(
        validators=[
            MinValueValidator(1969),
            MaxValueValidator(datetime.datetime.now().year)
        ],
        initial = 1997
    )

    NoEmp = forms.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20000)
        ],
        initial = 10
    )
    

