from django import forms
from imager_images.models import Album, Photo


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        widgets = {
            'photos': forms.CheckboxSelectMultiple,
        }

        fields = [
            'title',
            'description',
            'cover_photo',
            'photos',
        ]

    photos = forms.ModelMultipleChoiceField(
        queryset=Photo.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        photographer = kwargs.pop('photographer')
        super(EditAlbumForm, self).__init__(*args, **kwargs)
        q1 = Photo.objects.filter(photographer=photographer)
        self.fields['photos'].queryset = q1

    def save(self, commit=True):
        """enables photos to be saved"""
        photos = self.cleaned_data['photos']
        instance = super(EditAlbumForm, self).save(commit)
        instance.photos.add(*photos)
        return instance
