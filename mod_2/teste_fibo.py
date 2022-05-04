from fibo import fibonacci

class Test_fibo:
    def setup(self):
        pass

    def test_fibonacci(self):
        resultado = [1, 2, 3, 5, 8, 13, 21, 34, 55]

        assert resultado == [i for i in fibonacci(9)]