from src.main import add
import pytest

def test_add():
 """
  assert add(7, 2) == 
  assert add(5, "2", 3) == 
  assert add("2", "8.2") == 
  assert add("8", "1", 3.6) == 
  assert add("1", "2") == 
  assert add("3", "4", "5") == 
  assert add(2.6, "4", None) == 
  assert add(2.5, 3, "5.1") == 
  assert add(5.4, 9.8) == 
  assert add("1.4", "2", 3) == 
  assert add(2.5, 3, "x") == 
  assert add(2.1, 9.3, 3.7) == 
  assert add(1, 6, 3) == 
  assert add(1.6, 2.1) == 
  assert add(3.1, 2) == 
  assert add(1.9, 4.3, "2.6") == 
  assert add("1", "2", 9) == 
  assert add("4", "2.4", 1) == 
  assert add(None, 3, "5.1") == 
  assert add("b", 4, 5) == 
"""
    return