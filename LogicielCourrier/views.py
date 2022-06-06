from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from CourriersApp.models.my_model import Courrier

@login_required
def home_view(request):
    #return HttpResponse ('Logiciel gestion de courrier')
    return render(request, 'home.html')

@login_required
def courrierA_view(request): 
    #return HttpResponse ("Courrier Arrivés")
    return render(request, 'courrierArrives.html')

@login_required
def courrierD_view(request):
    return render(request, 'courrierDepart.html')
 
  
"""@login_required
def connexion(request):
    return render(request, 'connexion.html')"""

