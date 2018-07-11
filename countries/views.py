from django.shortcuts import render
from django.http import HttpResponse

#Vistas basadas en Funciones (Function Based View)
def home(request):
	return HttpResponse("En la vida, todo es una metáfora. Kafka en la orilla(2002)")
