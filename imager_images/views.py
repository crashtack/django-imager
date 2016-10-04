from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def library_view(request):

    current_user = User.objects.filter(username=request.user).first()
    images = current_user.photos.all()
    albums = current_user.albums.all()
    context = {'images': images, 'albums': albums}

    return render(request, 'imager_images/library.html', context)
