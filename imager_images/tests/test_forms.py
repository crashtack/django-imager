# Wednesday morning lecture
import tempfile
from django.conf import settings
from django.test import override_settings

TEST_MEDIA = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=TEST_MEDIA)
def test_upload(self):
    # make sure there are not photos in the DB
    pass
