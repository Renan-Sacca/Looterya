from django.shortcuts import render
from .models import fichas
def index(request):
    ficha = fichas.objects.all()
    
    dados={
        'fichas' : ficha
    }

    return render(request,'index.html', dados)
    

