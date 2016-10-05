from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from imager_images.models import Photo
from django.views.generic import ListView, DetailView, CreateView
from django.utils.decorators import method_decorator
from django.urls import reverse


@login_required
def library_view(request):

    current_user = User.objects.filter(username=request.user).first()
    images = current_user.photos.all()
    albums = current_user.albums.all()
    context = {'images': images, 'albums': albums}

    return render(request, 'imager_images/library.html', context)


@method_decorator(login_required, name='dispatch')
class UplaodPhotoView(CreateView):
    template_name = 'imager_images/upload_photo.html'
    model = Photo
    fields = ['title', 'description', 'file', 'photographer']
    success_url = '/images/library'


