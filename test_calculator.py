import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        assert 5 == calculator.subtract(6, 1)
