from django.urls import path
from . import view

urlpatterns = [ path("",view.one, name="home"),
                path("count/",view.two, name="count"),
                path("about/",view.three, name="about"),
               
    
]
