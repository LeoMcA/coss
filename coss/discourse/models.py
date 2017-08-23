from django.db import models
from django.conf import settings
from django.utils.timezone import now

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet

import requests

@register_snippet
class DiscourseCategory(models.Model):
    _category_id = models.PositiveSmallIntegerField()
    _name = models.CharField(max_length=50, blank=True, default='')
    _api_last_queried = models.DateTimeField(null=True)

    panels = [
        FieldPanel('category_id')
    ]

    class Meta:
        verbose_name_plural = 'discourse categories'

    def __str__(self):
        return str(self.name)

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._api_last_queried = None
        self._category_id = value

    @property
    def name(self):
        self._update()
        return self._name

    def _update(self):
        if self._api_last_queried is None or now - self._api_last_queried > 900:
            r = requests.get(f'{settings.DISCOURSE_URL}/c/{self.category_id}/show.json')
            show = r.json()
            self._name = show['category']['name']
            self._last_updated = now
