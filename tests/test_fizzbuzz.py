import pytest
from codigo.fizzbuzz import fizz_buzz

# given a list of numbers, return a string with the fizzbuzz result
def test_fizz_buzz():
    assert fizz_buzz([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
    ]


# given a number, return a string with the fizzbuzz result
def test_fizz_buzz_number_buzz():
    assert fizz_buzz([10]) == ["Buzz"]


def test_fizz_buzz_number_fizz():
    assert fizz_buzz([9]) == ["Fizz"]


def test_fizz_buzz_number_fizzbuzz():
    assert fizz_buzz([15]) == ["FizzBuzz"]


def test_fizz_buzz_number_number():
    assert fizz_buzz([1]) == ["1"]
