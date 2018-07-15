from django.shortcuts import render
from django.http import HttpResponse
"""from django.views.generic import View"""
##Comportamiento por defecto
from django.views.generic import TemplateView

#Vistas basadas en Funciones (Function Based View)
"""def home(request):
	return render(request, 'countries/home.html')"""

#Vistas basadas en Clases (Class Based View)
#class HomeView(View):
##Comportamiento por defecto
class HomeView(TemplateView):
	#Dependiendo el tipo de respuesta que necesitemos implementamos la funcion
	#get o post
	#def get(self, request, *args, **kwargs):
	#	return render(request, 'countries/home.html')
	##Comportamiento por defecto
	template_name = 'countries/home.html'
	def get_context_data(self, *args, **kwargs):
		countries = ['Francia', 'Croacia', 'Bélgica']
		return {'countries':countries}
