from django.shortcuts import render

# Create your views here.
def cdnmethod(request):
    return render(request, 'cdnmethod.html')

def parleg(request):
    return render(request, 'parleg.html')