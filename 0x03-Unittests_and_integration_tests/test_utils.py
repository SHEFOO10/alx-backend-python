#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from parameterized import parameterized
import requests


class TestAccessNestedMap(TestCase):
    """ Test Access Nested Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """ access nested map """
        result = access_nested_map(map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ('a'), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, map, path, exception):
        with self.assertRaises(exception):
            access_nested_map(map, path)


class TestGetJson(TestCase):
    """ TestGetJson """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ test get_json function """
        with patch('requests.get') as GetMocked:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            GetMocked.return_value = mock_response

            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            GetMocked.assert_called_once_with(test_url)
