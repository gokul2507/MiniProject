from .credentials import get_access
from django.shortcuts import redirect, render


data=get_access("14xGox9yPdCtGrOpgQszVPIKIcy2K24cNkkjci7mheUg")

def update(request):
    d = {}
    d["no_author"] = int(request.POST.get("no_author"))
    d["name"] = []
    for i in range(d["no_author"]):
        d["name"].append(request.POST.get("authorf"+str(i+1))+" "+request.POST.get("authorm"+str(i+1))+" "+request.POST.get("authorl"+str(i+1)))
    d["journal"] = request.POST.get("journal")
    d["paperid"] = request.POST.get("paperid")
    d["paper"] = request.POST.get("papername")
    d["edition"] = request.POST.get("paperedition")
    d["year"] = request.POST.get("year")
    d["startpage"] = request.POST.get("startpage")
    d["endpage"] = request.POST.get("endpage")
    # DATABASES
    data.insert_row([ d["paperid"],d["no_author"], ";".join(d["name"]),
    d["journal"],d["paper"], d["edition"], 
    d["year"], d["startpage"], d["endpage"]], 2)

def process(request):
    update(request=request)
    return redirect("home")


def sucess(request):
    return render(request, 'sucess.html')


