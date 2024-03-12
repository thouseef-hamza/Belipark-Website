from django.shortcuts import render,redirect
from django.views import View
from assets.models import Property
from home.forms import ContactUSForm
from django.http import JsonResponse
from .models import ContactUS,Blog,HomeGallery,Carousel,AboutUS,Faculty
from django.shortcuts import get_object_or_404
# Create your views here.

def homeView(request):
    if request.method == "GET":
        property_data=Property.objects.all()[:4]
        gallery_data=HomeGallery.objects.all().order_by("-id")
        carousels=Carousel.objects.all().order_by("-id")[:3]
        about_us=AboutUS.objects.last()
        faculties=Faculty.objects.all()
        context={
            "properties":property_data,
            "galleries":gallery_data,
            "carousels":carousels,
            "about_us":about_us,
            "faculties":faculties
        }
        return render(request,"home/home.html",context)


def aboutView(request):
    if request.method == "GET":
        about_details = AboutUS.objects.prefetch_related("directors").last()
        return render(request,"home/about_us.html",context={"about_details":about_details})

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
            phone_number=forms.cleaned_data.get("phone_number",""),
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

from assets.models import Infratech,InfraTechImages

def infratechPage(request):
    description=Infratech.objects.last()
    images=InfraTechImages.objects.all()
    return render(request, "home/infratech.html",context={"description":description.content if description else None,"images":images,"image_count":range(images.count())})

def infratechImage(request,id):
    image=get_object_or_404(InfraTechImages,id=id)
    
    return JsonResponse(
        {
            "message": "Image Fetched Successfully",
            "success": True,
            "status": 200,
        }
    )
