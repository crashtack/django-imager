from django.http import HttpResponse
from django.template import loader


def home_view(request):
    template = loader.get_template('imagersite/home.html')
    response_body = template.render()
    return HttpResponse(response_body)
