import pytest

from finite_field import ModuloFiveField


class TestModuloFiveField:
    @pytest.fixture(autouse=True)
    def modulo_five_field(self):
        self.f = ModuloFiveField()

    @pytest.mark.parametrize(
        'x, y, result',
        [(3, 4, 2), (0, 3, 3), (4, 1, 0), (2, 1, 3), (4, 4, 3)]
    )
    def test_successful_add(self, x, y, result):
        assert self.f.add(x, y) == result

    @pytest.mark.parametrize(
        'x, y, result',
        [(2, 3, 1), (4, 3, 2), (0, 4, 0), (4, 4, 1), (1, 2, 2)]
    )
    def test_successful_multiply(self, x, y, result):
        assert self.f.multiply(x, y) == result

    @pytest.mark.parametrize(
        'x, y',
        [(3, 5), (None, 1), (4.2, 2), (42, 21), (4, '4')]
    )
    def test_failed_add(self, x, y):
        with pytest.raises(ValueError):
            self.f.add(x, y)

    @pytest.mark.parametrize(
        'x, y',
        [(-3, 0), (None, 1), (4.2, 2), (42, 4), (4, '4')]
    )
    def test_failed_multiply(self, x, y):
        with pytest.raises(ValueError):
            self.f.multiply(-3, 0)
