def countries_data(request):
    france = {'name':'francia', 'pos':'Campeón',
              'map':'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/France_in_the_World_%28%2BEU%29.svg/250px-France_in_the_World_%28%2BEU%29.svg.png',
              'uniform':'https://media.uniformefc.com/media/catalog/product/cache/6/base/600x/17f82f742ffe127f42dca9de82fb58b1/3/1/312130c.jpg'}
    croatia = {'name':'croacia', 'pos':'Sub Campeón',
              'map':'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Croatia_in_European_Union.svg/250px-Croatia_in_European_Union.svg.png',
              'uniform':'https://assets.nike.com.br/ArquivoExibir/186687.jpg'}
    belgium = {'name':'bélgica', 'pos':'Tercer Lugar',
              'map':'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Belgium_in_European_Union.svg/250px-Belgium_in_European_Union.svg.png',
              'uniform':'https://media.uniformefc.com/media/catalog/product/cache/6/base/600x/17f82f742ffe127f42dca9de82fb58b1/b/e/belgium-home-shirt-2018.png'}

    countries = [france, croatia, belgium]
    return {'countries':countries}
