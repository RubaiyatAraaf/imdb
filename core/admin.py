from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _('IMDb')
admin.site.site_title = _('IMDb Admin Portal')
admin.site.index_title = _('IMDb Admin Portal')


class BaseAdmin(admin.ModelAdmin):
    """Base admin for all models using NameSlugStampedModel model"""
    readonly_fields = (
        'added_at', 'added_by', 'updated_at', 'updated_by', 'slug')
