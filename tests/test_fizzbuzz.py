from pytest import mark
from codigo.fizzbuzz import fizz_buzz

# given a list of numbers, return a string with the fizzbuzz result
@mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]),
        ([10], ["Buzz"]),
        ([9], ["Fizz"]),
        ([15], ["FizzBuzz"]),
        ([1], ["1"]),
    ],
)
def test_fizz_buzz(numbers, expected):
    assert fizz_buzz(numbers) == expected
