from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

#Vistas basadas en Funciones (Function Based View)
"""def home(request):
	return render(request, 'countries/home.html')"""

#Vistas basadas en Clases (Class Based View)
class HomeView(View):
	#Dependiendo el tipo de respuesta que necesitemos implementamos la funcion
	#get o post
	def get(self, request, *args, **kwargs):
		return render(request, 'countries/home.html')
