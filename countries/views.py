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

class UniformView(TemplateView):
	template_name = 'countries/uniform.html'

class CountryDetailView(TemplateView):
	template_name = 'countries/country_detail.html'

	def get_context_data(self, *args, **kwargs):
		code = kwargs['code']
		return {'code': code}

class CountryIdDetailView(TemplateView):
	template_name = 'countries/country_id_detail.html'

	def get_context_data(self, *args, **kwargs):
		code_id = kwargs['id']
		return {'id': code_id}
