from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from imager_images.models import Photo, Album
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse
from imager_images.form import EditAlbumForm


@login_required
def library_view(request):

    current_user = User.objects.filter(username=request.user).first()
    images = current_user.photos.all()
    albums = current_user.albums.all()
    context = {'images': images, 'albums': albums}

    return render(request, 'imager_images/library.html', context)


@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    template_name = 'imager_images/add_album.html'
    model = Album
    fields = ['title', 'description', 'published']
    success_url = '/images/library'

    def form_valid(self, form):
        """add user to new album"""
        form.instance.photographer = self.request.user
        return super(AddAlbumView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class UploadPhotoView(CreateView):
    template_name = 'imager_images/upload_photo.html'
    model = Photo
    fields = ['title', 'description', 'file', 'published',]
    success_url = '/images/library'

    def form_valid(self, form):
        """add user to new photo"""
        form.instance.photographer = self.request.user
        return super(UploadPhotoView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditPhoto(UpdateView):
    template_name = 'imager_images/edit_photo.html'
    model = Photo
    fields = ['title', 'description', 'published']
    success_url = '/images/library'


@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    form_class = EditAlbumForm
    template_name = 'imager_images/edit_album.html'
    success_url = '/images/library'
    queryset = Album.objects.all()

    def get_form_kwargs(self):
        kwargs = super(EditAlbumView, self).get_form_kwargs()
        kwargs.update({'photographer': self.request.user})
        return kwargs
