from django.shortcuts import render
from django.views import View
from assets.models import Property,Amenity
# Create your views here.

def homeView(request):
    if request.method == "GET":
        property_data=Property.objects.all()[:4]
        gallery_data=Amenity.objects.all()
        context={
            "properties":property_data,
            "galleries":gallery_data
        }
        return render(request,"home/home.html",context)
    

    
def aboutView(request):
    if request.method == "GET":
        return render(request,"home/about_us.html")