from django.http import HttpResponse
from django.template import loader


def home_view(request):
    template = loader.get_template('imagersite/home.html')
    context = {'request': request}
    response_body = template.render(context=context)
    # import pdb; pdb.set_trace()
    return HttpResponse(response_body)


def profile_view(request):
    template = loader.get_template('imager_profile/profile.html')
    response_body = template.render()
    return HttpResponse(response_body)
