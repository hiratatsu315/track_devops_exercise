from src.main import add
import pytest

def test_add():
  assert add(7, 2) == 9
  assert add(5, "2", 3) == "error"
  assert add("2", "8.2") == "error"
  assert add("8", "1", 3.6) == 84
  assert add("1", "2") == 12
  assert add("3", "4", "5") == 39
  assert add(2.6, "4", None) == "error"
  assert add(2.5, 3, "5.1") == "error"
  assert add(5.4, 9.8) == 15
  assert add("1.4", "2", 3) == "error"
  assert add(2.5, 3, "x") == "error"
  assert add(2.1, 9.3, 3.7) == 14
  assert add(1, 6, 3) == 10
  assert add(1.6, 2.1) == 3
  assert add(3.1, 2) == 5
  assert add(1.9, 4.3, "2.6") == "error"
  assert add("1", "2", 9) == 21
  assert add("4", "2.4", 1) == "error"
  assert add(None, 3, "5.1") == "error"
  assert add("b", 4, 5) == "error"
