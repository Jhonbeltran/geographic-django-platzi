from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ContinentsView(TemplateView):
    template_name = 'continents/continents.html'

class ContinentsIdDetailView(TemplateView):
	template_name = 'continents/continents_id_detail.html'

	def get_context_data(self, *args, **kwargs):
		code_id = kwargs['id']
		return {'id': code_id}
