import unittest

from precision import ASE, get_mean_absolute_scaled_error


class TestASE(unittest.TestCase):
    """
    TODO: Test negative values and more floats
    """
    def test_ASE_1(self):
        """
        Test the ASE method
        """
        value_1 = 8
        value_2 = 3
        training_set = [2, 3, 4, 3, 4, 5]
        m = 5
        mean_absolute_scaled_error = get_mean_absolute_scaled_error(training_set, m)
        result = ASE(value_1, value_2, mean_absolute_scaled_error)
        print("result:" + str(result))
        self.assertEqual(result, 5/3)

    def test_ASE_2(self):
        """
        Test the ASE method
        """
        value_1 = 9
        value_2 = 3
        training_set = [2, 3, 4, 3, 4, 5]
        m = 5
        mean_absolute_scaled_error = get_mean_absolute_scaled_error(training_set, m)
        result = ASE(value_1, value_2, mean_absolute_scaled_error)
        print("result:" + str(result))
        self.assertEqual(result, 2)

    def test_ASE_3(self):
        """
        Test the ASE method
        """
        value_1 = 8
        value_2 = 4
        training_set = [2, 3, 4, 3, 4, 5]
        m = 5
        mean_absolute_scaled_error = get_mean_absolute_scaled_error(training_set, m)
        result = ASE(value_1, value_2, mean_absolute_scaled_error)
        print("result:" + str(result))
        self.assertEqual(result, 4/3)

    def test_ASE_4(self):
        """
        Test the ASE method
        """
        value_1 = 8
        value_2 = 7
        training_set = [2, 3, 4, 3, 4, 5]
        m = 2
        mean_absolute_scaled_error = get_mean_absolute_scaled_error(training_set, m)
        result = ASE(value_1, value_2, mean_absolute_scaled_error)
        print("result:" + str(result))
        self.assertEqual(result, 1)

    def test_ASE_5(self):
        """
        Test the ASE method
        """
        value_1 = 6
        value_2 = 9
        training_set = [2, 3, 4, 3, 4, 5]
        m = 2
        mean_absolute_scaled_error = get_mean_absolute_scaled_error(training_set, m)
        result = ASE(value_1, value_2, mean_absolute_scaled_error)
        print("result:" + str(result))
        self.assertEqual(result, 3)

    def test_ASE_6(self):
        """
        Test the ASE method
        """
        value_1 = 1.13
        value_2 = 0.8
        training_set = [2, 3, 4, 3, 4, 5]
        m = 2
        mean_absolute_scaled_error = get_mean_absolute_scaled_error(training_set, m)
        result = ASE(value_1, value_2, mean_absolute_scaled_error)
        print("result:" + str(result))
        self.assertAlmostEqual(result, 0.33)

if __name__ == '__main__':
    unittest.main()
