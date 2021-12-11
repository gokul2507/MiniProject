import enum
from .credentials import get_access
from django.shortcuts import redirect, render


data=get_access("14xGox9yPdCtGrOpgQszVPIKIcy2K24cNkkjci7mheUg")
def update(request):
    if request.method=="POST" and request.POST.get("uid"):
        index=str(int(request.POST.get("uid"))+1)
        result=[]
        '''paperid	authorcount	name	journal	paper	edition	year	spage	epage'''
        result.append(request.POST.get("paperid"))
        result.append(str(request.POST.get("no_author")))
        name=[]
        for i in range(int(request.POST.get("no_author"))):
            name.append(request.POST.get("authorf"+str(i+1))+" "+request.POST.get("authorm"+str(i+1))+" "+request.POST.get("authorl"+str(i+1)))
        result.append(";".join(name))
        result.append(request.POST.get("journal"))
        result.append(request.POST.get("papername"))
        result.append(request.POST.get("paperedition"))
        result.append(request.POST.get("year"))
        result.append(request.POST.get("startpage"))
        result.append(request.POST.get("endpage"))
        cell_list=data.range('A'+index+":I"+index)
        
        for i,val in enumerate(result):
            cell_list[i].value=str(val)
        data.update_cells(cell_list=cell_list)
        print(result)
        # data.update("A"+index+":B"+index,["a","b","c","d","e","f","g","h","i"])
        pass
    return redirect("home")
def update_first(request):
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
    print(d)
    data.insert_row([ d["paperid"],str(d["no_author"]), ";".join(d["name"]),
    d["journal"],d["paper"], d["edition"], 
    d["year"], d["startpage"], d["endpage"]], 2)

def process(request):
    update_first(request=request)
    return redirect("home")


def sucess(request):
    return render(request, 'sucess.html')


