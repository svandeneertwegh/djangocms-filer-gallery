# coding: utf-8

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from filer.models import File

from .models import ImageGallery


class GalleryPlugin(CMSPluginBase):
    model = ImageGallery
    name = _("Image gallery")
    render_template = 'djangocms_gallery/gallery.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['gallery_name'] = instance.name
        context['gallery_images'] = File.objects.filter(folder_id=instance.folder_id)
        return context


plugin_pool.register_plugin(GalleryPlugin)
