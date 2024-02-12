from django.urls import path
from property import views

urlpatterns = [
    path("",views.PropertyListView.as_view(),name="property_list"),
    path("detail/",views.PropertyRetriveView.as_view(),name="property_detail")
]
