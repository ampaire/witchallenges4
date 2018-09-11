import unittest

from list_sum import list_sum, power_num


class day4Testcase(unittest.TestCase):
    def setUp(self):
        pass

    def test_list_sum(self):
        response = list_sum([1, 3, 5, 7, 9, [1, 2]])
        self.assertEqual(response, 28)

    def test_if_empty(self):
        response = list_sum([[]])
        self.assertEqual(response, 0)

    def test_ifString(self):
        with self.assertRaises(TypeError):
            list_sum('h')

    def test_ifList(self):
        response = list_sum([1, 3, 5, 7, 9, [1, 2]])
        self.assertRaises(TypeError, list_sum, (1, 2))

    def test_ifInteger(self):
        response = list_sum([1, 3, 5, 7, 9, [1, 2]])
        self.assertRaises(TypeError, list_sum, 'welcome')

    def test_ifNotInteger(self):
        response = power_num(2.6, -5)
        with self.assertRaises(TypeError):
            power_num(2.6, 'a')

    def text_isNot_string(self):
        response = power_num(7, -3)
        with self.assertRaises(TypeError):
            power_num(7, 'welcome')

    def test_ifPower_isZero(self):
        response = power_num(3, 0)
        self.assertEqual(response, 1)
        

if __name__ == '__main__':
    unittest.main()
