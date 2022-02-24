from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'poll/index.html')
    #return HttpResponse("<h1>안녕~ Django!!</h1>")

def cart(request):
    cart = "계란"
    cartlist = ["계란", "두부", "커피"]
    return render(
        request,
        'poll/cart.html',
        {'cart':cart, 'cartlist':cartlist}
    )
