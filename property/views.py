from django.shortcuts import render
from django.views import View
from property.models import Property,Projects
# Create your views here.

class PropertyListView(View):
    def get(self,request,*args, **kwargs):
        properties=Property.objects.all()
        return render(request,"property/property_list.html",context={"properties":properties})

class PropertyRetriveView(View):
    def get(self,request,id,*args, **kwargs):
        # property=Property.objects.get(id=id)
        return render(request,"property/property_detail.html",context={"property":property})

class ProjectListView(View):
    def get(self,request,*args, **kwargs):
        projects=Projects.objects.all()
        return render(request,"project/project_list.html",context={"projects":projects})

class ProjectRetriveView(View):
    def get(self, request, id, *args, **kwargs):
        project = Projects.objects.get(id=id)
        return render(
            request, "projects/projects_detail.html", context={"projects": project}
        )
