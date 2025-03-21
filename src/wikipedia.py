# v 0.1

class Wikipedia:
        """
        Ein Objekt, das Informationen über eine Wikipedia-Seite speichert.

        Attribute:
        titel (str): Der Titel der Wikipedia-Seite.
        link (str): Der API-Link zur HTML-Version der Seite.
        inhalt (str): Der Inhalt der Seite.
        ausgehende_links (list): Eine Liste von ausgehenden Links auf der Seite.
        eingehende_links (list): Eine Liste von eingehenden Links zur Seite.
        """

        def __init__(self, titel):
                self.titel = titel
                self.link = 'https://api.wikimedia.org/core/v1/wikipedia/de/page/' + self.titel + '/html'
                self.inhalt = ""
                self.eingehende_links = []
                self.ausgehende_links = []
