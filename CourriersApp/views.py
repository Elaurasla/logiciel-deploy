from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .formulaire import CourrierForm
from .formulaire import CourrierDepartForm

from .models.my_model import Courrier
from .models.my_model import CourrierDepart
from .models.my_model import CourrierFilter

from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from CourriersApp import models
#from CourriersApp.models import my_model
from django.http import HttpResponse
from django.template import loader

from django.contrib import admin
from comptes.decorators import group_required

#from django.db import my_model
#from .models.my_model import Courrier


@login_required
def index(request): 
    if request.method == "POST":
        form= CourrierForm(request.POST).save()
        return redirect('/courrier_arrive')
    form = CourrierForm()
    return render(request, 'index.html', {'form': form, 'dataCourriers':Courrier.objects.all()})

@login_required
def crr(request):
    if request.method == "POST":
        form = CourrierForm(request.POST, request.FILES)
        if form.is_valid():
            bureau = form.cleaned_data.get('bureau')
            try:
                form.save()
                return redirect ('crr')
            except:  
                pass
    else: 
        form = CourrierForm()
    return render(request, 'enregistrement_courrier.html', {'form': form})


@login_required
def view(request):
    courriers = Courrier.objects.all().order_by('-id')
    return render(request, "view.html", {'courriers':courriers})

@login_required
@group_required('admin')
def delete(request, id):
    courriers= Courrier.objects.get(id=id)
    if request.method == "POST":
        courriers.delete()
        return redirect('vue')
    context = {'courrier':courrier}
    return render(request, 'delete.html', context)

 

def update(request,id):
    courriers= Courrier.objects.get(id=id)
    form = CourrierForm(request.POST or None, instance= courriers)
    if form.is_valid():
        form.save()
        return redirect('vue')
    return render(request, 'update.html', {'form': form, 'courriers':courriers})

# def update(request,id):
#     courriers= Courrier.objects.get(id=id)
#     form= CourrierForm(instance = courriers)
#     if request.method == "POST":
#         form = CourrierForm(request_POST, instance= courriers)
#         if form.is_valid():
#             form.save()
#             return redirect('vue')
#     context = {'form': form}
#     return render(request, 'update.html', context)

# @login_required
# def update(request,id):
#     courriers= Courrier.objects.get(id=id)
#     form = CourrierForm(request.POST or None, instance=courriers)
#     if form.is_valid():
#         form.save()
#         return redirect('vue')
#     return render(request, 'update.html', {'form':form, 'courriers':courriers})

# @login_required
# def update(request,id):
#     courrier= Courrier.objects.get(id=id)
#     form = CourrierForm(request.POST or None, instance=courrier)
#     if form.is_valid():
#         form.save(courrier)
#         return redirect('vue')
#     return render(request, 'update.html', {'form':form})


# @login_required
# def update(request, id):
#     courrier = Courrier.objects.get(id=id)
#     if request.method == "POST":
#         form = CourrierForm(request.POST, instance= courrier)
#         if form.is_valid():
#             bureau = form.cleaned_data.get('bureau')
#             try:
#                 form.save()
#                 return redirect ('crr')
#             except:  
#                 pass
#     else: 
#         form = CourrierForm(instance=courrier)
#     return render(request, 'update.html', {'form': form,'courrier':courrier})

# @login_required
# def update(request, id):
#     courriers = Courrier.objects.get(id=id)
#     if request.method == 'POST':
#         form = CourrierForm(request.POST, instance= courriers)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("vue"+id)
#     else:
#         form = CourrierForm(instance=courriers)

#     return render(request, 'update.html', {'form':form, 'courriers':courriers})

# @login_required
# def update(request, id):
#     courrier = Courrier.objects.get(id=id)
#     if request.method == "POST":
#         form= CourrierForm(request.POST or None, instance=courrier).save()
#         return redirect('vue')
#     return render(request, 'update.html', {'courrier':courrier, 'form':form})


# @login_required
# def update(request, id):
#     courrier= Courrier.objects.get(id=id)
#     form = CourrierForm(request.POST or None, instance=courrier)
#     if form.is_valid():
#         form.save()
#         return redirect('/view')
#     return render(request, "update.html", {'courrier':courrier, 'form': form})


# @login_required
# def update(request,id):
#     courrier= Courrier.objects.get(id=id)
#     if request.method == "POST":
#         form = CourrierForm(request.POST or None, instance=courrier)
#         if form.is_valid():
#             bureau = form.cleaned_data.get('bureau')
#             try:
#                 form.save()
#                 return redirect ('/view')
#             except:  
#                 pass
#     else: 
#         form = CourrierForm()
#     return render(request, 'update.html', {'form': form})

# @login_required
# def update(request,id):
#     courrier= Courrier.objects.get(id=id)
#     form = CourrierForm(request.POST or None, instance=courrier)
#     if form.is_valid():
#         form.save()
#         return redirect('/view')
#     return render(request, 'update.html', {'courrier':courrier, 'form':form})


@login_required
def crr_depart(request):
    if request.method == "POST":
        form = CourrierDepartForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                message.success(request,'Courrier enregistré')
                return redirect ('/crrd')
            except:  
                pass
    else: 
        form = CourrierDepartForm()
    return render(request, 'courrierD_enregistrement.html', {'form': form})

@login_required
def view_depart(request):
    courriersdepart = CourrierDepart.objects.all().order_by('-id')
    return render(request, "viewdepart.html", {'courriersdepart':courriersdepart})


@login_required  
@group_required('admin')
def delete_depart(request, id):
    courriersdepart= CourrierDepart.objects.get(id=id)
    courriersdepart.delete()
    return redirect("/viewd")

@login_required
def update_depart(request,id):
    courriers= CourrierDepart.objects.get(id=id)
    form = CourrierDepartForm(request.POST or None, instance= courriers)
    if form.is_valid():
        form.save()
        return redirect('vued')
    return render(request, 'update_depart.html', {'form': form, 'courriers':courriers})


def image(request, id):
    image = Courrier.objects.all().get(id=id)
    return render(request, "imageA.html", {'image':image})
