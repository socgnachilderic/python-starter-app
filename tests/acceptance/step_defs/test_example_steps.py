"""Addition feature tests."""

from assertpy import assert_that
from pytest_bdd import given, parsers, scenarios, then, when

from domain.hello import Calculator

scenarios("../features/example.feature")


@given(
    parsers.parse("the numbers <{num1:d}> and <{num2:d}>"), target_fixture="calculator"
)
def the_numbers_1_and_3(num1: float, num2: float) -> Calculator:
    """the numbers 1 and 3."""
    return Calculator(num1, num2)


@when("they are added together")
def they_are_added_together(calculator: Calculator):
    """they are added together."""
    calculator.add()


@then(parsers.parse("should the result be <{expected:d}>"))
def should_the_result_be_4(calculator: Calculator, expected: float):
    """should the result be 4."""
    assert_that(calculator.get_result()).is_equal_to(expected)
