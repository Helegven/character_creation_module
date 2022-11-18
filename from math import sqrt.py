from math import sqrt

message: str = """
Добро пожаловать в самую
лучшую программу для вычисления
квадратного корня из заданного числа"""

print(message)


def CalculateSquareRoot(Number: int) -> int:
    """Вычисляет квадратный корень."""
    x: float = sqrt(Number)
    return print(f'Это будет: {x}')


def calc(your_number: float) -> float:
    """Проверяем число."""
    if your_number <= 0:
        return
    print("""Мы вычислили квадратный корень
          из введённого вами числа.""")
    CalculateSquareRoot(your_number)


calc(25.5)
