from django.shortcuts import render
import requests
from .models import APIData
from .import apitest
# import apitest

"""Getting api data from apitest.py and sending it to db """

# print(apitest.Model_ID)
# print(apitest.Make_ID)

# Create your views here.
def Details(request):
     context = {}
     return render(request, 'Website/Details.html', context)

def History(request):
     context = {}
     return render(request, 'Website/History.html', context)

def Results(request):
      context = {}
      return render(request, 'Website/Results.html', context)


# x = apitest.Model_ID
# y = apitest.Make_ID


def index(request):
     
     x = apitest.Model_ID
     y = apitest.Make_ID
 
     for i in range(0,14):
          value = APIData(

               Model_ID = x[i],
               Make_ID = y[i],
                )
          value.save()
     
     data = APIData.objects.all()
     return render(request,'Website/index.html',{'data': data})