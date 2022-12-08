from django.shortcuts import render
from datetime import date
from Appfamilia.models import familiar
from django.template import context, Template, loader
from django.http import HttpResponse
# Create your views here.


def familiares(request):

    fam1=familiar(nombre="Esteban", edad=20, fecha_de_nacimiento="2001-12-17")
    fam1.save()
    


    fam2=familiar(nombre="Armando", edad=50, fecha_de_nacimiento="1972-1-1")
    fam2.save()



    fam3=familiar(nombre="Mabel", edad=40, fecha_de_nacimiento="1982-2-7")
    fam3.save()
    listafamiliares={"fam1":fam1, "fam2":fam2, "fam3":fam3}
   

    return render(request,"plantilla1.html",listafamiliares )