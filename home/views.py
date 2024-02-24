from django.shortcuts import render,redirect
from django.views import View
from assets.models import Property
from home.forms import ContactUSForm
from django.http import JsonResponse
from .models import ContactUS,Blog,HomeGallery
from django.shortcuts import get_object_or_404
# Create your views here.

def homeView(request):
    if request.method == "GET":
        property_data=Property.objects.all()[:4]
        gallery_data=HomeGallery.objects.all().order_by("-id")
        context={
            "properties":property_data,
            "galleries":gallery_data
        }
        return render(request,"home/home.html",context)


def aboutView(request):
    if request.method == "GET":
        return render(request,"home/about_us.html")

def createContact(request):
    if request.method=="POST":
        forms=ContactUSForm(data=request.POST
                            )
        if not forms.is_valid():
            print(forms.errors)
            return JsonResponse(
                {"errors": forms.errors, "success": False, "status": 400}
            )
        ContactUS.objects.create(
            full_name=forms.cleaned_data["full_name"],
            email=forms.cleaned_data["email"],
            subject=forms.cleaned_data.get("subject",""),
            message=forms.cleaned_data["message"]   
        )
        return JsonResponse(
            {
                "message": "Form Submitted Successfully",
                "success": True,
                "status": 201,
            }
        )
    return redirect("home:home_view") 

def blogList(request):
    blogs=Blog.objects.all()
    return render(request,"blogs/blog_list.html",{"blogs":blogs})

def blogDetail(request,id):
    blog=get_object_or_404(Blog,id=id) 
    blogs=Blog.objects.all().order_by("-created_at")
    return render(request,"blogs/blog_detail.html",context={"blog":blog,"blogs":blogs})