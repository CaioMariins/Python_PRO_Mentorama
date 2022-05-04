import scrapy
import random

""" 
Este código passeia através de páginas da wikipédia enquanto encontra outras páginas
também da wiki, é um crawler semelhante ao do exercício mas randômico!

"""

class count():                  # coloquei essa classe aqui pra poder praticar mais sobre iteradores
    def __init__(self):        
        self.count = 0

    def __iter__(self):
        self.count = self.count
        return self

    def __next__(self):
        self.count += 1
        return self.count

c = count()

class Wiki(scrapy.Spider):

    name = "wikipedia"
    start_urls = ["https://pt.wikipedia.org/wiki/Not%C3%ADcia_falsa"]



    def parse(self, response):
        pag_name = response.css("head title::text").get()
        
        print("Página {}ª".format(next(c)), pag_name) #Executa o contador nas páginas.

        next_page = response.css('li a::attr(href)').getall()
        next_page = [i for i in next_page if "wiki" in i] #separa só links da wiki
        next_page = random.choice(next_page) #seleciona um link random para seguir
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

# caso a linha 37 seja retirada ele passeará por qualquer link encontrado, pode resultar em erros
# páginas inesperadas ou simplesmente fechar a spider porque o código fonte não bate com a 
# referência as tags li.

### CUIDADO! ESTE CÓDIGO PODE SER ONEROSO PARA SERVIDORES SEU USO SE FAZ SOMENTE PARA FINS DE ESTUDO!