from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"home/home.html")
    
    
def aboutView(request):
    if request.method == "GET":
        return render(request,"home/about_us.html")