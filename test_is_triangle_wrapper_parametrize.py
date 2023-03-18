# a + b , b + c , a + c . Первую сумму сравниваем с оставшейся стороной c , вторую - с a и третью - с b .
# Если хотя бы в одном случае сумма окажется не больше третьей стороны, то делается вывод, что треугольник не существует.
import pytest


def print_triangle(f=bool):
    def wrapper(*args):
        res = f(*args)
        print("Результат вызова функции:", res)
        return res
    return wrapper


@print_triangle
def is_triangle(a, b, c):
    if all((a + b > c, a + c > b, b + c > a)):
        return True
    else:
        return False


@pytest.mark.parametrize("a, b, c, d",
                         [(0, 2, 3, False), (-2, 3, 4, False), (100,2,4, False), (4,4,4, True), (3, 4, 5, True)])
def test_is_triangle(a, b, c, d):
    assert is_triangle(a, b, c) == d
