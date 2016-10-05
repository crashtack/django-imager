from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Photo, Album
from django.views.generic import CreateView


@login_required
def library_view(request):

    current_user = User.objects.filter(username=request.user).first()
    images = current_user.photos.all()
    albums = current_user.albums.all()
    context = {'images': images, 'albums': albums}

    return render(request, 'imager_images/library.html', context)


# @login_required
class AddAlbumView(CreateView):
    template_name = 'imager_images/add_album.html'
    model = Album
    fields = ['title', 'description', 'published', 'cover_photo']

    def get_successfull_url(self):
        import pdb; pdb.set_trace()
        self.object.photographer = self.request.user
        self.object.save()
        return reverse('album_detail', args=(self.object.pk,))
