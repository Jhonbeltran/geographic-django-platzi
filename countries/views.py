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

		france = {'name':'francia', 'pos':'Campeón',
				  'shield':'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/France_in_the_World_%28%2BEU%29.svg/250px-France_in_the_World_%28%2BEU%29.svg.png'}
		croatia = {'name':'croacia', 'pos':'Sub Campeón',
				  'shield':'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Croatia_in_European_Union.svg/250px-Croatia_in_European_Union.svg.png'}
		belgium = {'name':'bélgica', 'pos':'Tercer Lugar',
				  'shield':'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Belgium_in_European_Union.svg/250px-Belgium_in_European_Union.svg.png'}

		countries = [france, croatia, belgium]
		return {'countries':countries}
