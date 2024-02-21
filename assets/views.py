from django.shortcuts import render,redirect
from django.views import View
from assets.models import Property,Project
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def propertiesList(request):
    if request.method == "GET":
        properties=Property.objects.all()
        return render(request,"property/property_list.html",context={"properties":properties})
    else:
        return redirect("home:home_view")

def getDetailProperty(request,id):
    if request.method == "GET":
        property_data=get_object_or_404(Property,id=id)
        context={
            "property_name":property_data.property_name,
            "property_address":property_data.address,
            "property_price":property_data.price,
            "description":property_data.description,  
            "image":property_data.main_photo,
            "images":property_data.property_images.all()          
        }
        return render(request,"property/property_detail.html",context=context)
    else:
        return redirect("home:home_view")

class ProjectListView(View):
    def get(self,request,*args, **kwargs):
        projects=Project.objects.all()
        return render(request,"projects/project_list.html",context={"projects":projects})

class ProjectRetriveView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            project = Project.objects.prefetch_related("project_images").filter(id=id).first()
        except Project.DoesNotExist:
            pass
        context = {
            "project_name": project.project_name,
            "description": project.description,
            "amenity": project.amenity.all(),
            "services": project.service.all(),
            "images": project.project_images.all(),
        }
        return render(
            request, "projects/project_detail.html", context=context
        )
