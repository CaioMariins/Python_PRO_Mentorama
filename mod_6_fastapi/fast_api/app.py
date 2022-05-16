from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Bem vindo a api de operações básicas, cheque a documentação e o método POST: math. Para checar a documentação utilize /docs ao final da url"}

class Resp(BaseModel):
    valor1: int
    valor2: int
    operacao: str


@app.post("/math")
async def math(resp: Resp):
    """
    Para executar uma operação basta selecionar o símbolo matemático usual para ela:
    adição = +,
    subtração = -,
    multiplicação = x,
    divisão = %,
    """
    if resp.operacao == "+":
        return{"Soma":resp.valor1 + resp.valor2}
    if resp.operacao == "-":
        return{"Subtração":resp.valor1 - resp.valor2}
    if resp.operacao == "x":
        return{"Multiplicação":resp.valor1 * resp.valor2}
    if resp.operacao == "%":
        return{"Divisão":resp.valor1 / resp.valor2}
    else:
        return{"Message":"Selecione uma opção correta, caso esteja tendo problemas verifique a documentação"}

