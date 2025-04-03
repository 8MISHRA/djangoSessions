from django.shortcuts import render

# Create your views here.
def allChai(request):
    return render(request, "chai/all_chai.html")

def order(request):
    return render(request, "chai/order.html")