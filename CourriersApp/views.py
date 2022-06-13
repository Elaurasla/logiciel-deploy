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

# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

# import datetime
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
# from django.db.models import Sum

#from django.db import my_model
#from .models.my_model importCourrier



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
    courriers =Courrier.objects.all().order_by('-id')
    return render(request, "view.html", {'courriers':courriers})

@login_required
@group_required('admin')
def delete(request, id):
    courriers=Courrier.objects.get(id=id)
    if request.method == "POST":
        courriers.delete()
        return redirect('vue')
    context = {'courrier':courrier}
    return render(request, 'delete.html', context)

 

def update(request,id):
    courriers=Courrier.objects.get(id=id)
    form = CourrierForm(request.POST or None, instance= courriers)
    if form.is_valid():
        form.save()
        return redirect('vue')
    return render(request, 'update.html', {'form': form, 'courriers':courriers})


@login_required
def crr_depart(request):
    if request.method == "POST":
        form = CourrierDepartForm(request.POST, request.FILES)
        if form.is_valid():
            bureau = form.cleaned_data.get('bureau')
            try:
                form.save()
                return redirect ('crrd')
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
    image = Currier.objects.all().get(id=id)
    return render(request, "imageA.html", {'image':image})


# def courrier_pdf(request):
#     buf = io.BytesIO()
#     c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     textob=c.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont("Helvetica", 14)


#     courriers = Courrier.objects.all()

#     lines=[]
    
#     for Courrier in courriers:
#         lines.append(Courrier.num)
#         lines.append(Courrier.date)
#         lines.append(Courrier.date_emission)
#         lines.append(Courrier.reference)
#         lines.append(Courrier.origine)
#         lines.append(Courrier.objet)
#         lines.append(Courrier.bureau)
#         lines.append(Courrier.obs)

#     for line in lines:
#         textob.textLine(line)

#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)

#     return FileResponse(buf, as_attachment="True", filename="Courrier.pdf")

# def telecharger_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition']="inline; attachment; filename=Expenses"+ \
#         str(datetime.datetime.now())+'.pdf'
#     response['Content-Transfer-Enoding']='binary'

#    Courrier =Courrier.objects.filter(owner=request.user)
    
#     sumCourrier.aggregate.filter(Sum('amount'))

#     html_string=render_to_string("pdf-output.html", {Courrier'Courrier,'total':sum})
#     html=HTML(string=html_string)

#     results=html.write_pdf()

#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(results)
#         output.flush()
#         output=open(output.name, 'rb')
#         response.write(output.read())