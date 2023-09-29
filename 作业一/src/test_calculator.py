import unittest
from Calculation import *


class TestCalculator(unittest.TestCase):
    

    def test_calculate_science(self):
        # 测试calculate_science函数的功能

        # 测试综合加法、减法、乘法和除法
        deal=Calculation()
        result = deal.evaluate('-2+2-3x4÷2')
        self.assertEqual(result, -6)

        # 测试带有括号的表达式
        result = deal.evaluate('(2+(3x4))% 8 x2^2')
        self.assertEqual(result, 24)

        # 测试科学计算函数 - 正弦值、平方根、自然对数综合
        result = deal.evaluate('sin(45)+√(16)-ln(e)+cos(45)+tan(45)')
        self.assertAlmostEqual(result, 5.4142, places=4)

        # 测试科学计算函数 asin,acos,atan,atan
        result = deal.evaluate('asin(0.5)+acos(0.5)+atan(1)')
        self.assertAlmostEqual(result, 2.35619, places=4)

        # 测试科学计算函数 log,
        result = deal.evaluate('lg(10)')
        self.assertAlmostEqual(result, 1, places=4)

        # 测试科学计算函数 - 阶乘
        result = deal.evaluate('1+5!')
        self.assertEqual(result, 121)

        # 测试阶乘嵌套括号
        result = deal.evaluate('2+(3x(4-1)!)')
        self.assertEqual(result, 20)

        # 测试科学计算函数 - 正弦值嵌套平方根
        result = deal.evaluate('√(sin(45))')
        self.assertAlmostEqual(result, 0.8409, places=4)

        # 测试科学计算函数 - 对数嵌套阶乘
        result = deal.evaluate('ln(5!)xπ')
        self.assertAlmostEqual(result, 15.0403, places=4)
        
        # 测试正弦值嵌套阶乘
        result = deal.evaluate('√(sin(5!))')
        self.assertAlmostEqual(result, 0.9306, places=4)

        result = deal.evaluate('1-(-(4+2!))')
        self.assertAlmostEqual(result, 7, places=4)

        #测试运算符所需参数不够的错误
        with self.assertRaises(ValueError):
                deal.evaluate('1+')

        #测试阶乘时参数为负数的错误
        with self.assertRaises(ValueError):
                deal.evaluate('(-1)!')
        
        # with self.assertRaises(ValueError):
        #         deal.evaluate('180!')
