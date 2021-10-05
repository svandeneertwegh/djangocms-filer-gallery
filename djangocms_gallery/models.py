from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.models import Folder


class ImageGallery(CMSPlugin):
    name = models.CharField(verbose_name=_('Gallery name'), max_length=255)
    folder = models.ForeignKey(Folder, verbose_name=_('Folder'), related_name='gallery_folder', on_delete=models.CASCADE, help_text=_("Select folder with gallery images."))

    class Meta:
        ordering = ['pk']
        verbose_name = _('Image gallery')
        verbose_name_plural = _('Image galleries')

    def __str__(self):
        return f'{self.name}'
