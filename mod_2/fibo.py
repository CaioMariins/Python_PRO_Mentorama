class fibonacci():
    """
    Cria um iterador para a sequência fibonnaci.
    n = Número de iterações que deseja fazer.
    """

    def __init__(self,n): #inicializador
        self.anterior = 0
        self.proximo = 1
        self.iteration = n

    def __iter__(self): #iterador
        
        self.anterior = self.anterior # atualiza o anterior para ser possível gerar próximos números

        return self

    def __next__(self):
        if self.iteration != 0 or self.iteration > 0: #condicional para execução do código.
            self.soma = self.anterior + self.proximo
            self.anterior = self.proximo
            self.proximo = self.soma
            self.iteration -= 1
            return self.proximo
        else:
            raise StopIteration

fibo_ord = { i : j for i,j in enumerate(fibonacci(10))} #demonstra o dict compreension

print("\n sequência enumerada no dicionário: \n")
print("=="*40)
print(fibo_ord)
print("=="*40)