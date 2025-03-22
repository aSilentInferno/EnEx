# v 0.2.4

import json
import requests
import os
from dotenv import load_dotenv
from wikipedia import Wikipedia

load_dotenv()

api_token = os.getenv("WIKI_ACCESS_TOKEN")

if api_token is None:
    raise ValueError("WIKI_ACCESS_TOKEN environment variable is not set")

headers = {
        'Authorization': 'Bearer ' + api_token,
        'User-Agent': 'EnEx (kajwich@icloud.com)'
        }

def get_wiki_page(name: str):
    """
    Holt die HTML-Datei einer Wikipedia-Seite mittels einer API-Anfrage.

    :param name: Der Name der Wikipedia-Seite.
    :return: Der Text der Antwort der API-Anfrage innerhalb eines Wikipedia-Objekts.
    """
    url = 'https://api.wikimedia.org/core/v1/wikipedia/de/page/' + name + '/html'
    response = requests.get(url, headers=headers)
    wiki = Wikipedia(name)
    wiki.inhalt = response.text
    return wiki

    

def _get_inbound_links(name: str):
    """
    Holt die eingehenden Links einer Wikipedia-Seite mittels einer API-Anfrage.

    :param name: Der Name der Wikipedia-Seite.
    :return: Die Antwort der API-Anfrage als JSON-Objekt.
    """
    url = 'https://de.wikipedia.org/w/api.php?action=query&format=json&prop=linkshere&titles=' + name + '&formatversion=2&lhlimit=max'
    response = requests.get(url).json()
    
    # Die Dictionary die Wikipedia zurpckgibt hat einenkomischen aufbau mit sehr viel verschachtelung
    linksdictionary = response["query"]["pages"]["linkshere"]

    # filere Links die wir nicht haben wollen
    links = [_["title"] for _ in linksdictionary if not (_["title"].startswith(("Benutzer:", "Wikipedia:", "Vorlage:", "Hilfe", "redirect:", "Special:", "Kategorie:")))]
    
    return links


def _get_outbound_links(name: str):
    """
    Holt die ausgehenden Links einer Wikipedia-Seite mittels einer API-Anfrage.

    :param name: Der Name der Wikipedia-Seite.
    :return: Die Antwort der API-Anfrage als JSON-Objekt.
    """
    url = 'https://de.wikipedia.org/w/api.php?action=query&prop=links&titles=' + name + '&pllimit=max&format=json'
    response = requests.get(url).json()
    
    # Die Dictionary die Wikipedia zurpckgibt hat einenkomischen aufbau mit sehr viel verschachtelung
    linksdictionary = next(iter(response["query"]["pages"].values()))["links"]

    # filere Links die wir nicht haben wollen
    links = [_["title"] for _ in linksdictionary if not (_["title"].startswith(("Benutzer:", "Wikipedia:", "Vorlage:", "Hilfe:", "Special", "Kategorie:")))]
    
    return links

def get_wiki_links(name: str):
    """
    Holt die eingehenden und ausgehenden Links einer Wikipedia-Seite mittels einer API-Anfrage.

    :param name: Der Name der Wikipedia-Seite.
    :return: Die eingehenden und ausgehenden Links als JSON-Objekte innerhalb eines Wikipedia-Objekts.
    """
    inbound_links = _get_inbound_links(name)
    outbound_links = _get_outbound_links(name)
    wiki = Wikipedia(name)
    wiki.eingehende_links = inbound_links
    wiki.ausgehende_links = outbound_links
    return wiki
