import requests
import json
from client import *


# Função para buscar informações de um anime específico
def get_anime_details(ranking,fields=None,filename='anime_details.json'):
    url = f"https://api.myanimelist.net/v2/anime/ranking"
    headers = {
        "X-MAL-CLIENT-ID": CLIENT_ID
    }
    params = {
        "ranking_type" : {ranking},
        "limit" : 20
    }

    if fields:
        params['fields'] = fields

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print(f"Error: {response.status_code} - {response.text}")

def get_anime_titles_airing():
    titles = []
    response = get_anime_details("airing")
    if response:
        for anime in response['data']:
            titles.append(anime['node']['title'])
        return titles
    
def get_anime_titles_upcoming():
    titles = []
    response = get_anime_details("upcoming")
    if response:
        for anime in response['data']:
            titles.append(anime['node']['title'])
        return titles