from django.test import TestCase

from coss.discourse.tests import DiscourseCategoryFactory

from unittest.mock import patch, PropertyMock

class DiscourseCategoryTests(TestCase):
    def setUp(self):
        self.category = DiscourseCategoryFactory.create()

    @patch('coss.discourse.models.DiscourseCategory.name', new_callable=PropertyMock)
    def test___str__(self, name):
        name.return_value = 'Category Name'

        self.assertEqual(str(self.category), 'Category Name')

    @patch('coss.discourse.models.DiscourseCategory._show')
    def test_name(self, _show):
        name = 'Category Name'
        _show.return_value = { 'category': { 'name': name } }

        assert self.category.name is name

    @patch('coss.discourse.models.settings')
    @patch('coss.discourse.models.DiscourseCategory._cached_request')
    def test__show(self, _cached_request, settings):
        value = 'value'
        _cached_request.return_value = value
        settings.DISCOURSE_URL = 'http://discourse'

        assert self.category._show() is value
        _cached_request.assert_called_once_with('http://discourse/c/198/show.json')

    @patch('coss.discourse.models.cache')
    @patch('coss.discourse.models.requests')
    def test__cached_request(self, requests, cache):
        path = 'path'
        value = 'value'

        cache.get.return_value = value

        assert self.category._cached_request(path) is value
        cache.get.assert_called_once_with(path)

        cache.get.return_value = None
        requests.get.return_value.json.return_value = value

        assert self.category._cached_request(path) is value
        requests.get.assert_called_once_with(path)
