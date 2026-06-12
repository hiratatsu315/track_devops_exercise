from src.main import add
import pytest

def test_add():
    # --- 1. 型チェックの検証（-1 を返すケース） ---
    # aが数値以外
    assert add("5", 5, 5) == -1
    assert add(None, 5, 5) == -1
    # bが数値以外
    assert add(5, "5", 5) == -1
    assert add(5, [5], 5) == -1
    # cが数値以外
    assert add(5, 5, "5") == -1

    # --- 2. 境界値・範囲チェックの検証（-2 を返すケース） ---
    # aの境界値（0未満、10より大きい）
    assert add(-0.1, 5, 5) == -2
    assert add(-1, 5, 5) == -2
    assert add(10.1, 5, 5) == -2
    assert add(11, 5, 5) == -2
    
    # bの境界値
    assert add(5, -0.1, 5) == -2
    assert add(5, 10.1, 5) == -2

    # cの境界値
    assert add(5, 5, -0.1) == -2
    assert add(5, 5, 10.1) == -2

    # --- 3. 正常系の検証（計算結果が正しいか） ---
    # 境界値の成功パターン (0 と 10)
    assert add(0, 0, 0) == 0
    assert add(10, 10, 10) == 30 # int(10+10) + int(10)

    # cが省略された場合（c=0として動作するか）
    assert add(5, 2) == 7
    assert add(10, 10) == 20

    # 小数が含まれる場合の特有の計算ロジックの検証
    # 実装が int(a + b) + int(c) のため、その通りの結果になるか確認
    # 例: int(1.5 + 2.6) + int(0) = 4 + 0 = 4
    assert add(1.5, 2.6) == 4
    
    # 例: int(1.5 + 2.6) + int(1.2) = 4 + 1 = 5
    assert add(1.5, 2.6, 1.2) == 5
    
    # a, b, c すべてがfloatで正常な範囲
    assert add(5.5, 4.5, 9.9) == 19 # int(10.0) + int(9.9) = 10 + 9 = 19
