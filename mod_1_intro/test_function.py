from function import check_n

class Test_function:
    def setup(self):
        pass
    
    def test_mult_5(self):
        resultado = check_n(5)
        
        assert resultado == (None,"fizz")

    def test_mult_7(self):
        resultado = check_n(14)

        assert resultado == (None,"buzz")

    def test_mult_both(self):
        resultado = check_n(70)

        assert resultado == (None,"fizzbuzz")
        
    def test_multh_null(self):
        resultado = check_n(13)

        assert resultado == (None,"miss")