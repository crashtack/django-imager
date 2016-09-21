from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout


def home_view(request):
    template = loader.get_template('imagersite/home.html')
    response_body = template.render()
    return HttpResponse(response_body)


# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.
