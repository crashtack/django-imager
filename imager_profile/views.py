from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Photographer
from django import forms



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
    fields = ['first_name', 'last_name', 'email']
    success_url = '/profile/'

    def get_object(self):
        return self.request.user

    def get_form(self, *args, **kwargs):
        form = super(EditProfileView, self).get_form(*args, **kwargs)
        form.fields['bio'] = forms.fields.CharField(initial=self.object.photographer.bio)
        return form

    def form_valid(self, form):
        """add bio to valid form"""
        form.instance.photographer.bio = form.cleaned_data.get('bio')
        form.instance.photographer.save()
        return super(EditProfileView, self).form_valid(form)



