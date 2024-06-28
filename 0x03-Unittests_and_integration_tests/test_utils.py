#!/usr/bin/env python3
from unittest import TestCase
from utils import access_nested_map
from parameterized import parameterized


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
