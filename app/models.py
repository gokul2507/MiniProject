from re import sub
from .credentials import get_access
from django.http import JsonResponse
from django.core import serializers

data=get_access("14xGox9yPdCtGrOpgQszVPIKIcy2K24cNkkjci7mheUg")
class GETDATA:
     def __init__(self):
          self.sheet_data=data.get_all_records()
          pass
     def contain(self,main_str,sub_str):
          sub_str=sub_str.lower()
          if sub_str==str(main_str.get("paperid","")).lower() or sub_str==str(main_str.get("year","")).lower() or sub_str==str(main_str.get("edition","")).lower():
               return 1
          return sub_str in str(main_str.get("name","")).lower() or sub_str in str(main_str.get("journal","")).lower() or sub_str in str(main_str.get("paper","")).lower()
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