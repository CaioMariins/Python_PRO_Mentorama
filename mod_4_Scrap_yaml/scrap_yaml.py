import scrapy
import re


class Yaml(scrapy.Spider):

    name = "Yaml"
    start_urls = ["https://www.w3schools.io/file/yaml-sample-example/"]
    def parse(self, response):
        coments = response.css("div.highlight code.language-Yaml span.c::text").getall() #apenas os comentários
        yaml = response.css("div.highlight code.language-Yaml span::text").getall() #Todo exemplo

        clean = [re.findall(r"\w+",i) for i in coments]
        
        final = []
        for i in clean:
            final.append(" ".join(i))
    
        print(final) #comentários sem as #

        with open("yaml_example.yaml", "w") as f:
            for i in yaml:
                f.write(i)
        

# Não sei se entendi bem o que era pra ser feito com o regex. Mas o resultado final é o output do yaml!