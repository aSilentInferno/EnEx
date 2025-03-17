# v 0.1.2
# 2025-03-16

import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv("WIKI_ACCESS_TOKEN")

headers = {
        'Authorization': 'Bearer ' + api_token,
        'User-Agent': 'EnEx (kajwich@icloud.com)'
        }

class Wikipedia:
    def __init__(self, name: str):
        """
        Initialisiert eine neue Instanz der Wikipedia-Klasse.

        :param name: Der Name der Wikipedia-Seite.
        """
        self.name = name
        self.url = 'https://api.wikimedia.org/core/v1/wikipedia/en/page/' + self.name + '/html'

    def fetch(self):
        """
        Holt die HTML-Datei der Wikipedia-Seite mittels einer API-Anfrage.

        :return: Der Text der Antwort der API-Anfrage.
        """
        response = requests.get(self.url, headers=headers)
        return response.text