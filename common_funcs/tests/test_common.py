import unittest

from django.test import TestCase
from common_funcs.common import is_number, is_integer, calculate_regression, remove_html_tags

class TestIsNumber(TestCase):
    def setUp(self):
        pass

    def test_is_number_with_integer(self):
        self.assertTrue(is_number("123"))

    def test_is_number_with_float(self):
        self.assertTrue(is_number("123.45"))

    def test_is_number_with_negative_integer(self):
        self.assertTrue(is_number("-123"))

    def test_is_number_with_negative_float(self):
        self.assertTrue(is_number("-123.45"))

    def test_is_number_with_non_numeric_string(self):
        self.assertFalse(is_number("abc"))

    def test_is_number_with_empty_string(self):
        self.assertFalse(is_number(""))

    def test_is_number_with_whitespace(self):
        self.assertFalse(is_number("   "))

    def test_is_number_with_special_characters(self):
        self.assertFalse(is_number("$123"))


class TestCommonFunctions(TestCase):
    def setUp(self):
        pass
    
    def test_is_integer(self):
        self.assertTrue(is_integer("123"))
        self.assertTrue(is_integer("-123"))
        self.assertTrue(is_integer("0"))
        self.assertFalse(is_integer("123.45"))
        self.assertFalse(is_integer("abc"))
        self.assertFalse(is_integer(""))


class TestCalculateRegression(TestCase):
    def setUp(self):
        pass

    def test_calculate_regression_with_linear_data(self):
        data = {'set1': [1, 2, 3, 4, 5]}
        result = calculate_regression(data, 'set1')
        self.assertAlmostEqual(result['set1'][0], 1.0)  # slope
        self.assertAlmostEqual(result['set1'][1], 1.0)  # intercept

    def test_calculate_regression_with_constant_data(self):
        data = {'set1': [5, 5, 5, 5, 5]}
        result = calculate_regression(data, 'set1')
        self.assertAlmostEqual(result['set1'][0], 0.0)  # slope
        self.assertAlmostEqual(result['set1'][1], 5.0)  # intercept

    def test_calculate_regression_with_negative_slope(self):
        data = {'set1': [5, 4, 3, 2, 1]}
        result = calculate_regression(data, 'set1')
        self.assertAlmostEqual(result['set1'][0], -1.0)  # slope


    def test_calculate_regression_with_multiple_sets(self):
        data = {
            'set1': [1, 2, 3, 4, 5],
            'set2': [2, 4, 6, 8, 10]
        }
        result = calculate_regression(data, 'set1')
        self.assertAlmostEqual(result['set1'][0], 1.0)  # slope
        self.assertAlmostEqual(result['set1'][1], 1.0)  # intercept
        self.assertAlmostEqual(result['set2'][0], 2.0)  # slope


class TestCommonFunctions(TestCase):
    def setUp(self):
        pass

    def test_remove_html_tags(self):
        self.assertEqual(remove_html_tags("<p>Hello</p>"), "Hello")
        self.assertEqual(remove_html_tags("<div><p>Test</p></div>"), "Test")
        self.assertEqual(remove_html_tags("<a href='#'>Link</a>"), "Link")
        self.assertEqual(remove_html_tags("No tags"), "No tags")
        self.assertEqual(remove_html_tags("<p>Multiple <b>tags</b> here</p>"), "Multiple tags here")
