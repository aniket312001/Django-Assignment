from django.urls import path,include
from . import views 

urlpatterns = [
    path('list/',views.index,name="index"),
    path('<str:pk>/newProduct/',views.newProductForm,name="newproduct"),

]
