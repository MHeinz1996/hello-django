"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from math import pi

def rectangle_area_query(request):
    try:
        height = request.GET.get('height')
        width = request.GET.get('width')
        area = int(height) * int(width)
        response = HttpResponse(f"<p>Area of a rectangle with height: {height} and width: {width} = {area}</p>")
        return response
    except:
        response = HttpResponse()
        response.status_code = 400
        return response

def rectangle_area(request, height: int, width: int):
    area = height*width
    response = HttpResponse(f"<p>Area of a rectangle with height: {height} and width: {width} = {area}</p>")
    return response

def rectangle_perimeter(request, height, width):
    perimeter = (2*height) + (2*width)
    response = HttpResponse(f"<p>Perimeter of a rectangle with height: {height} and width: {width} = {perimeter}</p>")
    return response

def circle_area(request, radius):
    area = pi * radius * radius
    response = HttpResponse(f"<p>Area of a circle with radius: {radius} = {area}</p>")
    return response

def circle_perimeter(request, radius):
    perimeter = 2 * pi * radius
    response = HttpResponse(f"<p>Perimeter of a circle with radius: {radius} = {perimeter}</p>")
    return response
    

urlpatterns = [
    path('rectangle/area/query', rectangle_area_query),
    path('rectangle/area/<int:height>/<int:width>', rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>', rectangle_perimeter),
    path('circle/area/<int:radius>', circle_area),
    path('circle/perimeter/<int:radius>', circle_perimeter),
    path('admin/', admin.site.urls),
]
