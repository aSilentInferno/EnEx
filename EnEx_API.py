# v 0.1.1
# 2025-03-13

import requests  # Importiert das requests-Modul für HTTP-Anfragen
import os  # Importiert das os-Modul für Betriebssystem-Funktionen
from dotenv import load_dotenv  # Importiert load_dotenv, um Umgebungsvariablen aus einer .env-Datei zu laden

load_dotenv()  # Lädt Umgebungsvariablen aus einer .env-Datei

api_token = os.getenv("WIKI_ACCESS_TOKEN")  # Holt den API-Token aus den Umgebungsvariablen

# Definiert die Header für die HTTP-Anfrage
headers = {
        'Authorization': 'Bearer ' + api_token,  # Setzt den Authorization-Header
        'User-Agent': 'EnEx (kajwich@icloud.com)'  # Setzt den User-Agent-Header
        }

class Wikipedia:
    def __init__(self, name: str):
        """
        Initialisiert eine neue Instanz der Wikipedia-Klasse.

        :param name: Der Name der Wikipedia-Seite.
        """
        self.name = name  # Setzt den Namen der Wikipedia-Seite
        self.url = 'https://api.wikimedia.org/core/v1/wikipedia/en/page/' + self.name + '/html'  # Setzt die URL für die API-Anfrage

    def fetch(self):
        """
        Holt die HTML-Datei der Wikipedia-Seite mittels einer API-Anfrage.

        :return: Der Text der Antwort der API-Anfrage.
        """
        response = requests.get(self.url, headers=headers)  # Führt eine GET-Anfrage an die API durch
        return response.text  # Gibt den Text der Antwort zurück