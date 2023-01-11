from django.shortcuts import render
from django.http import HttpResponse
import time
from bs4 import BeautifulSoup
from requests import get
from asyncio import sleep as sleep_async
from random import shuffle
from collections import Counter
import re


def comp_list(lista2,lista1):
    """Compara listas the outputs das funções de request. Para evitar requests
    duplicados durante o processo.

    Args:
        lista2 (list): lista anterior
        lista1 (list): lista do output do processo atual.

    Returns:
        list: lista sem repetições.
    """

    list_no_repeat = [i for i in lista2 if i not in lista1]
    return list_no_repeat

async def tratamento(lista):
    """Trata os links com regex para aceitar apenas links https durante a procura.

    Args:
        lista (list): Lista de links

    Returns:
        list: Lista final de links tratados.
    """
    lista_final = []
    for link in lista:
        if re.findall(r"[a-zA-Z]+://", str(link)):
            lista_final.append(link)
    print(lista_final)
    return lista_final


async def first_request(url):
    """Efetua requets de forma assíncrona para os sites escolhidos e colhe links das páginas.
    As outras funções funcionam igual a essa. funcionam igual.

    Args:
        url (string): url com HTTP

    Returns:
        list: lista com todas os links encontrados.
    """
    if url != None:
        try:
            first_results = []
            #First requests:
            resp = get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            for link in soup.find_all('a', href=True,limit=10):
                first_results.append(link.get('href'))
            shuffle(first_results) #embaralha os links para não seguir sempre a mesma ordem de caminho:
            print("========"*20,"\n",first_results)
            print("========"*20,"\n")
        except:
            print("Algo deu errado!")
    return first_results

    #Second requests
async def second_request(first_results):
    results_2 = []
    for link in first_results:
        resp_2 = get(link)
        print("Request on:",link)
        await sleep_async(1)
        soup_2 = BeautifulSoup(resp_2.text,"html.parser")
        for link_2 in soup_2.find_all('a', href=True,limit=3):
            results_2.append(link_2.get("href"))
        shuffle(results_2)
    print("========"*20,"\n",results_2)
    print("========"*20,"\n")
    return results_2

    #Third requests
async def third_request(second_results):
    results_3 = []
    for link in second_results:
        resp_3 = get(link)
        #await sleep_async(1)
        soup_3 = BeautifulSoup(resp_3.text,"html.parser")
        for link_3 in soup_3.find_all('a', href=True,limit=3):
            results_3.append(link_3.get("href"))
        shuffle(results_3)
    print("========"*20,"\n",results_3)
    print("========"*20,"\n")
    return results_3

    #Fourth requests
async def fourth_request(third_results):
    results_4 = []
    for link in third_results:
        resp_4 = get(link)
        #await sleep_async(1)
        soup_4 = BeautifulSoup(resp_4.text,"html.parser")
        for link_4 in soup_4.find_all('a', href=True,limit=3):
            results_4.append(link_4.get("href"))
        shuffle(results_4)
    print("========"*20,"\n",results_4)
    print("========"*20,"\n")
    return results_4

    #fifth requests
async def fifty_request(fourth_results):
    results_5 = []
    for link in fourth_results:
        resp_5 = get(link)
        #await sleep_async(1)
        soup_5 = BeautifulSoup(resp_5.text,"html.parser")
        for link_5 in soup_5.find_all('a', href=True,limit=3):
            results_5.append(link_5.get("href"))
        shuffle(results_5)
    print("========"*20,"\n",results_5)
    print("========"*20,"\n")
    return results_5

async def main(url):
    """Função principal que organiza em etapas os processos anteriores. E faz seleção dos links mais comuns

    Args:
        url (string): url

    Returns:
        list: resultado final
    """
    lista_final = []

    first_results = await first_request(url)
    first_results = await tratamento(first_results)

    second_results = await second_request(first_results) #Faz o request e salva a lista
    second_results = await tratamento(second_results) #trata urls
    second_results = comp_list(first_results,second_results) #evita links repetidos

    third_results = await third_request(second_results)
    third_results = await tratamento(third_results)
    third_results = comp_list(second_results,third_results)

    fourth_results = await fourth_request(third_results)
    fourth_results = await tratamento(fourth_results)
    fourth_results = comp_list(third_results,fourth_results)

    fifty_results = await fifty_request(fourth_results)
    fifty_results = await tratamento(fifty_results)

    lista_final_ = first_results + second_results + third_results + fourth_results + fifty_results

    c = Counter(lista_final_)
    return c.most_common(10)


import asyncio  #estranhamente não funciona se não importar aqui.

def home(request):
    """ Renderização no Django"""
    context = {}
    if request.method == "POST":
        url = request.POST.get('url')
        lista_final = asyncio.run(main(url))
        context['lista_final'] = lista_final
    return render(request, 'home.html', context=context )
