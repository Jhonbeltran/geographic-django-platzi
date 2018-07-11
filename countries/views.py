from django.shortcuts import render
from django.http import HttpResponse

#Vistas basadas en Funciones (Function Based View)
def home(request):
	return render(request, 'countries/home.html')
