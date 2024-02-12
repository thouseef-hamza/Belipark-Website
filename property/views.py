from django.shortcuts import render
from django.views import View
# Create your views here.

class PropertyListView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"property/property_list.html")
    
class PropertyRetriveView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"property/property_detail.html")