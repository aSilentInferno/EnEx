# v 0.1

import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv("WIKI_ACCESS_TOKEN")

headers = {
        'Authorization': 'Bearer ' + api_token,
        'User-Agent': 'EnEx (kajwich@icloud.com)'
        }


# Das Wikipedia Objekt zum Speichern von der Wikipedialinks

class Wikipedia:

    def __init__(self, titel):
        self.titel = titel
        self.link = 'https://api.wikimedia.org/core/v1/wikipedia/en/page/' + self.titel + '/html'

    

# link -> done
# inhalt
# ausgehendeLinks 
# eingehendeLinks

def fetch(site: Wikipedia):
        """
        Holt die HTML-Datei der Wikipedia-Seite mittels einer API-Anfrage.

        :return: Der Text der Antwort der API-Anfrage.
        """
        response = requests.get(site.link, headers=headers)
        return response.text
