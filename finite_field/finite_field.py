import abc
import numbers


class AbstractFiniteField(abc.ABC):
    """Абстрактный класс конечного поля"""

    @abc.abstractmethod
    def add(self, x, y):
        """Операция сложения для элементов поля"""

    @abc.abstractmethod
    def multiply(self, x, y):
        """Операция умножения для элементов поля"""


class ModuloFiveField(AbstractFiniteField):
    """Конечное поле, в котором операции сложения и умножения вычисляются по модулю 5"""

    def add(self, x, y):
        """
        >>> f = ModuloFiveField()
        >>> f.add(3, 4)
        2
        >>> f.add(4.2, 21)
        Traceback (most recent call last):
        ...
        ValueError: math domain error
        >>> f.add(42, 3)
        Traceback (most recent call last):
        ...
        ValueError: math domain error
        """

        if (not isinstance(x, numbers.Integral) or
                not isinstance(y, numbers.Integral)
                or x % 5 != x or y % 5 != y):
            raise ValueError('math domain error')

        return (x + y) % 5

    def multiply(self, x, y):
        """
        >>> f = ModuloFiveField()
        >>> f.multiply(2, 3)
        1
        >>> f.multiply(4.2, 21)
        Traceback (most recent call last):
        ...
        ValueError: math domain error
        >>> f.multiply(42, 3)
        Traceback (most recent call last):
        ...
        ValueError: math domain error
        """

        if (not isinstance(x, numbers.Integral) or
                not isinstance(y, numbers.Integral)
                or x % 5 != x or y % 5 != y):
            raise ValueError('math domain error')

        return (x * y) % 5
