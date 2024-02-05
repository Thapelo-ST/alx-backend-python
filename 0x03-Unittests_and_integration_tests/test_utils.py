#!/usr/bin/env python3
"""Documenting the whole testing classes
"""
import unittest
from unittest.mock import patch, Mock, MagicMock
from typing import Dict
from parameterized import parameterized
from utils import access_nested_map, memoize
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Testing all the nested map class

    Args:
        unittest (TestCase): tests the Nested Map

    Raises:
        KeyError: key error
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        tests the accessed nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    """Tests the execption errors

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to access in the nested map.

        Raises:
            KeyError: If the access operation results in a KeyError.
    """
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests the execption errors

        Args:
            nested_map
            path

        Raises:
            KeyError
        """
        with self.assertRaises(KeyError):
            value = nested_map
            for key in path:
                if isinstance(value, dict):
                    value = value[key]
                else:
                    raise KeyError(key)


class TestGetJson(unittest.TestCase):
    """
    tests the get_json function in the unittest cases
    """
    @patch('requests.get')
    def test_get_json(self, mock_get):
        """test_get_json

        Args:
            mock_get (dict): mock values
        """
        # Define test cases
        test_cases = [
            {"test_url": "http://example.com",
                "test_payload": {"payload": True}},
            {"test_url": "http://holberton.io",
                "test_payload": {"payload": False}},
        ]

        # testing over test cases
        for case in test_cases:
            with self.subTest(case=case):
                # getting test data
                test_url = case["test_url"]
                test_payload = case["test_payload"]

                # create a Mock object for the response
                mock_response = Mock()

                mock_response.json.return_value = test_payload

                mock_get.return_value = mock_response

                # Call the function to test
                result = get_json(test_url)

                mock_get.assert_called_once_with(test_url)

                # Assert that the result is equal to the expected test_payload
                self.assertEqual(result, test_payload)

                # Reset the mock for the next iteration
                mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """Test Memoize used to test memoize function

    Args:
        unittest (TestCase): test the memoize function
    """

    def test_memoize(self):
        """Test memoize function
        """
        class TestClass:
            """Test class testing the properties
            """
            def a_method(self):
                """gets a method

                Returns:
                    int
                """
                return 42

            @memoize
            def a_property(self):
                """sets a method

                Returns:
                    method: setting the method get before
                """
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Mock the a_method
        with patch.object(test_instance, 'a_method',
                          return_value=42) as mock_a_method:
            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that a_method was called only once
            mock_a_method.assert_called_once()

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
