from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Photographer


@login_required
def profile_view(request):

    current_user = User.objects.filter(username=request.user).first()
    num_images = current_user.photos.all().count()
    num_albums = current_user.albums.all().count()
    context = {'num_images': num_images, 'num_albums': num_albums}

    return render(request, 'imager_profile/private_profile.html', context)


@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    template_name = 'imager_profile/edit_profile.html'
    model = User
    # import pdb; pdb.set_trace()
    fields = ['first_name', 'last_name', 'email']
    success_url = '/profile/'

    def get_object(self):
        # import pdb; pdb.set_trace()
        return self.request.user

    def form_valid(self, form):
        """add user to new photo"""
        form.instance.user = self.request.user
        return super(EditProfileView, self).form_valid(form)
