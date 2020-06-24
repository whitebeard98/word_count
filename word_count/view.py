from django.http import HttpResponse
from django.shortcuts import render 
import operator
def  one(request):
    return render(request,"view.html",{"china_matsuoka":"best ever body"})
def two(request):
    var=request.GET["input"]
    words=var.split()
    no_words=len(words)
    dict={}
    for i in words:
        if i not in dict.keys():
            dict[i]=1
        else:
            dict[i]+=1
    
    sorted_dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)    
    return render(request,"counted.html",
                  {"input":var,
                   "counted":sorted_dict,
                   "no_words":len(words)})
    
def three(request):
    return render(request,"about.html")