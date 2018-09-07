import unittest

from day4challenge import list_sum, power_num


class day4Testcase(unittest.TestCase):
    def setUp(self):
        pass

    def test_list_sum(self):
        response =list_sum([1, 3, 5, 7, 9, [1, 2]])
        self.assertEqual(response, 28)

    def test_ifList(self):
        response = list_sum([1, 3, 5, 7, 9, [1, 2]])
        self.assertRaises(TypeError,list_sum, 'welcome')

    def test_ifInteger(self):
        response =list_sum([1, 3, 5, 7, 9, [1, 2]])
        self.assertRaises(TypeError,list_sum, 'welcome')

    def test_ifInteger(self):
        response=power_num((2.6,-5))
        self.assertRaises(TypeError,power_num, 'a')

    def test_if




if __name__ == '__main__':
    unittest.main()
