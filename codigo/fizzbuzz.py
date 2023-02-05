from typing import List


def fizz_buzz(lst: List[int]) -> List[str]:
    result = []
    for n in lst:
        if n % 3 == 0 and n % 5 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(n))
    return result


if __name__ == "__main__":
    result = fizz_buzz([10])

    print(result)
