from src.main import add
import pytest

class TestAddFunction(unittest.TestCase):
    
    ### 1. 正常系のテスト（型も範囲も正しく、計算結果が返るケース）###
    def test_valid_integers(self):
        # 通常の整数
        self.assertEqual(add(5, 5, 5), 15)
        # 境界値：下限 (0)
        self.assertEqual(add(0, 0, 0), 0)
        # 境界値：上限 (10)
        self.assertEqual(add(10, 10, 10), 30)
    
    def test_default_argument(self):
        # cを省略した場合（デフォルト値 c=0 が適用されるか）
        self.assertEqual(add(5, 5), 10)
        
    def test_valid_floats_with_truncation(self):
        # 小数の場合（現在の仕様 int(a + b) + int(c) 通りの計算になるか）
        # 例: a=1.5, b=1.5, c=1.5 の場合
        # int(1.5 + 1.5) + int(1.5) = int(3.0) + 1 = 3 + 1 = 4 となる
        self.assertEqual(add(1.5, 1.5, 1.5), 4)

    ### 2. 型チェックのエラーテスト（-1 が返るケース）###
    def test_invalid_types(self):
        # それぞれの引数に文字列やNoneを渡した場合
        self.assertEqual(add("5", 5, 5), -1, "aが文字列の場合")
        self.assertEqual(add(5, "5", 5), -1, "bが文字列の場合")
        self.assertEqual(add(5, 5, "5"), -1, "cが文字列の場合")
        self.assertEqual(add(None, 5, 5), -1, "Noneが含まれる場合")
        self.assertEqual(add([1], 5, 5), -1, "リストが含まれる場合")

    ### 3. 境界値チェックのエラーテスト（-2 が返るケース）###
    def test_out_of_bounds(self):
        # a の境界値外（下限より小さい、上限より大きい）
        self.assertEqual(add(-1, 5, 5), -2)
        self.assertEqual(add(11, 5, 5), -2)
        
        # b の境界値外
        self.assertEqual(add(5, -0.1, 5), -2) # 小数での範囲外
        self.assertEqual(add(5, 10.1, 5), -2)
        
        # c の境界値外
        self.assertEqual(add(5, 5, -1), -2)
        self.assertEqual(add(5, 5, 11), -2)

if __name__ == '__main__':
    unittest.main()
