from requests import get, post
from json import loads

class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok

    def test_APIresponse(self):
        resp = get(self.url)
        message = loads(resp.text)
        assert message["message"] == "Bem vindo a api de operações básicas, cheque a documentação e o método POST: math!"

    def test_ADICAO(self):
        resp = post(self.url + "/math", json = {"valor1":10,"valor2":5,"operacao":"+"})
        message = loads(resp.text)
        esperada = {"Soma":15}
        assert message == esperada
    
    def test_SUB(self):
        resp = post(self.url + "/math", json = {"valor1":10,"valor2":5,"operacao":"-"})
        message = loads(resp.text)
        esperada = {"Subtração":5}
        assert message == esperada
    
    def test_MULTI(self):
        resp = post(self.url + "/math", json = {"valor1":10,"valor2":5,"operacao":"x"})
        message = loads(resp.text)
        esperada = {"Multiplicação":50}
        assert message == esperada
    
    def test_DIV(self):
        resp = post(self.url + "/math", json = {"valor1":10,"valor2":5,"operacao":"%"})
        message = loads(resp.text)
        esperada = {"Divisão":2}
        assert message == esperada
