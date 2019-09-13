from week_1.Functional.Power_of_Two import Power_of_twoBL
import unittest


class test_Power_of_twoBL(unittest.TestCase):

    # def test_2D_array(self):
    #     result = Power_of_twoBL.cal()
    #     self.assertEquals( 10,result)

    def test_Power_of_twoBL(self):
        result = Power_of_twoBL.cal()
        expected = 10
        self.assertEqual(expected, result)

if __name__ == '__main__':
    test_Power_of_twoBL()