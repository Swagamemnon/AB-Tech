import pytest
from employee import Employee

@pytest.fixture
def employee_for_testing():
    """Defines a default employee for testing other employee methods."""
    employee_for_testing = Employee('noah', 'decker', 50000)
    return employee_for_testing

def test_give_default_raise(employee_for_testing):
    """Tests whether salary increases by 5000"""
    employee_for_testing.give_raise()
    assert employee_for_testing.salary == 55000

def test_give_custom_raise(employee_for_testing):
    """Tests whether salary increases by correct custom ammount"""
    employee_for_testing.give_raise(increase=12000)
    assert employee_for_testing.salary == 62000

