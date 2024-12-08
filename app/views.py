from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'name':'Adhi','age':22,'Status':'single','maturity':'no'}
    return render(request,'conditions.html',context=d)
