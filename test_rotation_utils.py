"""
test_rotation_utils.py
Lance Thongsavanh
Write a complete pytest test suite in test_rotation_utils.py that verifies the adjust_rotation function from rotation_utils.py is working correctly.
Date.
"""

import pytest
from rotation_utils import adjust_rotation

"""
Your test file must achieve "full coverage" by including a dedicated test_ function for each of the following scenarios:
Input: 100 -> Expected Output: 100
Input: 460 -> Expected Output: 100
Input: 820 -> Expected Output: 100
Input: -100 -> Expected Output: 260
Input: -460 -> Expected Output: 260
Input: -820 -> Expected Output: 260
Non-Numeric Input: You must write a test that uses pytest.raises(TypeError) to verify the function correctly raises a TypeError when given a string (e.g., "abc").
"""

# positive test case
def test_adjust_rotation_positive_int() -> None:
    assert adjust_rotation(100) == 100
    assert adjust_rotation(460) == 100
    assert adjust_rotation(820) == 100

#negative test cases

#TypeError test case