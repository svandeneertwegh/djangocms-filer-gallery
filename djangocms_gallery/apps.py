from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GalleryConfig(AppConfig):
    name = 'djangocms_gallery'
    verbose_name = _('Gallery')
