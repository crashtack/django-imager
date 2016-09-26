from django.http import HttpResponse
from django.template import loader
from imager_images.models import Photo
from django.db.models import Q
from django.shortcuts import render


q1 = Q(published='public')
q2 = Q(published='shared')

query = q1 | q2


def home_view(request):
    if request.user.is_authenticated:
        photo = Photo.objects.filter(query).order_by('?').first()
    photo = Photo.objects.filter(q1).order_by('?').first()
    context = {'request': request, 'photo': photo, 'message': 'filepath'}

    return render(request, 'imagersite/home.html', context=context)


def profile_view(request):
    template = loader.get_template('imager_profile/profile.html')
    response_body = template.render()
    return HttpResponse(response_body)
