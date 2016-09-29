from django.shortcuts import render
from django.contrib.auth.models import User


def profile_view(request):

    current_user = User.objects.filter(username=request.user).first()
    num_images = current_user.photos.all().count()
    num_albums = current_user.albums.all().count()
    context = {'num_images': num_images, 'num_albums': num_albums}

    return render(request, 'imager_profile/profile.html', context)
