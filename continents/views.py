from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ContinentsView(TemplateView):
    template_name = 'continents/continents.html'

    def get_context_data(self, *args, **kwargs):
        america = {'name': 'América', 'quantity': 8, 'semifinalist': 0}
        europe = {'name': 'Europa', 'quantity': 14, 'semifinalist': 4}
        asia = {'name': 'Asia', 'quantity': 4, 'semifinalist': 0 }
        oceania = {'name': 'Oceanía', 'quantity': 1, 'semifinalist': 0}
        africa = {'name': 'África', 'quantity': 5, 'semifinalist': 0 }
        continents = [america, europe, asia, oceania, africa]
        return{'continents':continents}
