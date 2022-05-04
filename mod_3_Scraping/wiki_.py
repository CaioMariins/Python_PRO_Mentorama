import scrapy

""" ATENÇÃO: Este código pode ser bem agressivo fazendo muitos requests num intervalo curto de tempo!"""

class Wiki(scrapy.Spider):

    name = "wikipedia"
    
    def start_requests(self):
        yield scrapy.Request("https://pt.wikipedia.org/wiki/Not%C3%ADcia_falsa", self.parse)

    def parse(self, response):
        pag_name = response.css("head title::text").get() #Pega o título da página:

        print("Primeira página:",pag_name)

        next_page = response.css('li a::attr(href)').getall() #Recupera a maior parte dos links referentes a wiki
        list_pages = [i for i in next_page if "wiki" in i] #separa só links da wiki
        yield from response.follow_all(list_pages, callback=self.parse_all) #executa a função abaixo pra cada link

    def parse_all(self, response):
        pag_name = response.css("head title::text").get()
        print("Página secundária:",pag_name)
        