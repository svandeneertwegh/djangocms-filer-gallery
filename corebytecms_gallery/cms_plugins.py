# coding: utf-8

"""
    djangocms-widgets
    ~~~~~~~~~~~~~~~~~

    :copyleft: 2015 by the djangocms-widgets team, see AUTHORS for more details.
    :created: by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from filer.models import File

from .models import ImageGallery


class GalleryPlugin(CMSPluginBase):
    model = ImageGallery
    name = _("Image gallery")
    # text_enabled = True
    render_template = 'corebytecms_gallery/gallery.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['gallery_name'] = instance.name
        context['gallery_images'] = File.objects.filter(folder_id=instance.folder_id)
        return context


plugin_pool.register_plugin(GalleryPlugin)
