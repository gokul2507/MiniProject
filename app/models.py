from .credentials import get_access
from django.http import JsonResponse
from django.core import serializers

data=get_access("14xGox9yPdCtGrOpgQszVPIKIcy2K24cNkkjci7mheUg")
class GETDATA:
     def __init__(self):
          self.sheet_data=data.get_all_records()
          pass
     def contain(self,main_str,sub_str):
          if sub_str==main_str.get("paperid","") or sub_str==main_str.get("year","") or sub_str==main_str.get("edition",""):
               return 1
          return sub_str in main_str.get("name","") or sub_str in main_str.get("journal","") or sub_str in main_str.get("paper","")
     def getdata(self,tags):
          result_data=[]
          index=1
          for i in self.sheet_data:
               for t in tags:
                    if self.contain(i,str(t)):
                         result_data.append(str(index))
                         break
               index+=1
          return result_data