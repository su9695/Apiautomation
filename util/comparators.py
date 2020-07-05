import pytest

def get_uniform_comparator(comparator):
    if comparator in ["eq", "equals", "==", "is"]:
        return "equals"
def equal(self, check_value,expect_value):
    assert check_value == expect_value

