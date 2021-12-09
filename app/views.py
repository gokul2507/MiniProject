import re
from django.shortcuts import redirect, render
import openpyxl
from django.http import HttpResponse
# from .forms import create_form
from .models import GETDATA
from .update import process,sucess
from .excel import excel
from .credentials import get_access

data=get_access("14xGox9yPdCtGrOpgQszVPIKIcy2K24cNkkjci7mheUg")
def home(request):
    print(request.method)
    if request.method=="POST":
        get_data=GETDATA()
        if len(request.POST.getlist("tags[]"))==0:
                 return HttpResponse("none")
        resultdata=get_data.getdata(request.POST.getlist("tags[]"))
        return HttpResponse("-".join(resultdata))
    print("not passed")
    sheet_data=data.get_all_records()
    for i in sheet_data:
        i["name"]=i["name"].split(";")
    content={"context":sheet_data}
    return render(request, "home.html", content)


def index(request):
     return render(request, 'index.html')


def display(request):
    if request.POST and request.POST.get("id"):
        row_data=data.row_values(int(request.POST.get("id"))+1)
        row_data[2]=row_data[2].split(";")
        content={"content":row_data,"uid":request.POST.get("id")}
        return render(request,'display.html',content)
        pass
    return redirect('home')

def edit(request):
    print(request.POST)
    if request.POST and request.POST.get('id'):
        row_data=data.row_values(int(request.POST.get("id"))+1)
        row_data[2]=row_data[2].split(";")
        for i in range(int(row_data[1])):
                t=row_data[2][i].split()
                if len(t)==2:
                    t=t[:1]+[" "]+t[1:]
                row_data[2][i]=t
                
        content={"content":row_data,"uid":request.POST.get("id")}
        return render(request,'edit.html',content)
    return redirect('home')
