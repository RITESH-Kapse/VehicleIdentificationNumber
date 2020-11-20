from django.shortcuts import render

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