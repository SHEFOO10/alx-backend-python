#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from parameterized import parameterized
import requests
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
          self,
          map: Dict,
          path: Tuple[str],
          expected: Union[Dict, str]
          ) -> None:
        """ access nested map """
        result = access_nested_map(map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ('a'), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(
          self,
          map: Dict,
          path: Tuple[str],
          exception: Exception
          ) -> None:
        with self.assertRaises(exception):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """ TestGetJson """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(
          self,
          test_url: str,
          test_payload: Dict,
          mock_get: Mock
          ) -> None:
        """ test get_json function """
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """TestMemoize"""
    def test_memoize(self) -> None:
        """ test_memoize """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
            TestClass,
            'a_method',
            return_value: lambda: 42,
        ) as mock_fn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mock_fn.assert_called_once()
