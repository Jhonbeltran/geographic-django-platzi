from django.urls import reverse

def continents_data(request):

    america = {'name': 'América', 'quantity': 8, 'semifinalist': 0,'id':10,
               'detail_url': reverse("continents:id_detail", kwargs={'id':10})}
    europe = {'name': 'Europa', 'quantity': 14, 'semifinalist': 4,'id':20,
               'detail_url': reverse("continents:id_detail", kwargs={'id':20})}
    asia = {'name': 'Asia', 'quantity': 4, 'semifinalist': 0,'id':30,
               'detail_url': reverse("continents:id_detail", kwargs={'id':30})}
    oceania = {'name': 'Oceanía', 'quantity': 1, 'semifinalist': 0,'id':40,
               'detail_url': reverse("continents:id_detail", kwargs={'id':40})}
    africa = {'name': 'África', 'quantity': 5, 'semifinalist': 0,'id':50,
               'detail_url': reverse("continents:id_detail", kwargs={'id':50})}

    continents = [america, europe, asia, oceania, africa]
    return{'continents':continents}
