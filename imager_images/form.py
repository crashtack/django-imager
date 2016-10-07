from django import forms
from imager_images.models import Album, Photo


class AlbumEditForm(forms.ModelForm):
    class Meta:
        model = Album
        widgets = {
            'photos': forms.CheckboxSelectMultiple,
        }

        fields = [
            'photos',
        ]

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user')
    #     super(AlbumEditForm, self).__init__(*args, **kwargs)
    #     q1 = Photo.objects.filter(user=user)
    #     self.fields['photos'].querset = q1
