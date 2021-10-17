from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect

chal={ "jan":"do Django course",
    "feb": "walk 100 m",
    "march":" suggest to frends on challenge",
    "april":"month to rest",
    "may": "run for 30 min"
}

# Create your views here.
def home(request):
    data= list(chal.keys())
    if request.method =='POST':
        f_data=request.POST
        name= f_data['name']
        email=f_data['email']
        college= f_data['college']
        contact = f_data['no']
        loc = f_data['loc']
        hresp = "<p>"+name+ email +college+contact+loc+ "<p>"
        return HttpResponse(hresp)
        #return render(request,'monthlych/index.html',{'data':data,'color':'red'})
    #return HttpResponse("<h1>iam inside chal</h1>")
    elif request.method =='GET':
        return render(request,'monthlych/index.html',{'data':data,'color':'black'})

def regis(request):
    return render(request,'monthlych/register.html')
