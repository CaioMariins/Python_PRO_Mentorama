import asyncio
from aiohttp import ClientSession

"""
    Este código retorna todo o texto das páginas fazendo o scraping de forma assíncrona.
    Foi feito da forma mais simples e rápido possível seguindo o exemplo da aula e o exemplo contigo
    na documentação da aiohttp.
"""

urls = [
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-05-11",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-05-12",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-05-13",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-05-14",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-05-15",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-05-16",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-05-17",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-05-18",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-04-19",
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/2022-04-20",
]


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def simple_scraper():
    tasks = []
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        [print(t) for t in responses]


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(simple_scraper())
loop.run_until_complete(future)

