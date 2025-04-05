# test_sort_function.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from package_sort import sort

def test_returns_standard_for_non_bulky_and_non_heavy():
    assert sort(99, 100, 100, 10) == 'STANDARD'

def test_returns_special_for_bulky_but_not_heavy():
    assert sort(150, 200, 10, 10) == 'SPECIAL'

def test_returns_special_for_bulky_but_not_heavy2():
    assert sort(100, 100, 100, 10) == 'SPECIAL'

def test_returns_special_for_not_bulky_but_heavy():
    assert sort(99, 100, 100, 20) == 'SPECIAL'

def test_returns_rejected_for_bulky_and_heavy():
    assert sort(10, 10, 150, 20) == 'REJECTED'

def test_returns_rejected_for_bulky_and_heavy2():
    assert sort(100, 100, 100, 20) == 'REJECTED'