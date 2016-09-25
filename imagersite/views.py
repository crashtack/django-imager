from django.http import HttpResponse
from django.template import loader
from imager_images.models import Photo
from django.db.models import Q


q1 = Q(published='published')
q2 = Q(published='shared')

query = q1 | q2


def home_view(request):
    template = loader.get_template('imagersite/home.html')
    # if request.user.is_authenticated:
    #     photo = Photographer.objects.filter(published='published').order_by('?').first()
    photo = Photo.objects.filter(published='public').order_by('?').first()

    context = {'request': request, 'photo': photo, 'message': 'hello!'}
    response_body = template.render(context=context)
    # import pdb; pdb.set_trace()
    return HttpResponse(response_body)


def profile_view(request):
    template = loader.get_template('imager_profile/profile.html')
    response_body = template.render()
    return HttpResponse(response_body)
