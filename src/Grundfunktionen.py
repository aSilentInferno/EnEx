## Autor: Clemens Stein
## Funktionen: Stoppuhr, Random Wiki URL, Punktecounter, Titelextrahierung


from urllib.parse import urlparse, unquote
import math
import time
import threading


class Stoppuhr:
    def __init__(self):
        self.startzeit = None
        self.laufend = False
        self.thread = None
        self.verstrichene_zeit = 0

    def start(self):
        
        """Startet die Stoppuhr und setzt sie zurück"""
        
        self.startzeit = time.time()
        self.laufend = True
        self.verstrichene_zeit = 0
        ## print("Stoppuhr gestartet.")
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def _run(self):
        
        """Läuft im Hintergrund und aktualisiert die verstrichene Zeit."""
        
        while self.laufend:
            self.verstrichene_zeit = int(time.time() - self.startzeit)
            ## print(f"Sekunden: {self.verstrichene_zeit}", end="\r")
            time.sleep(1)

    def stop(self):
        
        """Stoppt die Stoppuhr."""
        
        self.laufend = False
        if self.thread:
            self.thread.join()
        ## print("\nStoppuhr gestoppt.")

    def get_zeit(self):
        
        """Gibt die aktuell verstrichene Zeit zurück."""
        
        return self.verstrichene_zeit


def random_Wiki_URL():
    
    """ Gibt eine zufällige Wikipedia URL als String aus """
    a = "https://de.wikipedia.org/wiki/Spezial:Zuf%C3%A4llige_Seite"
    return a
    

def wikipedia_title(url: str) -> str:
    
    """
    Extrahiert die Überschrift eines Wikipedia-Artikels aus der URL
    
    param url: Die zu analysierende Wikipedia-URL
    return: Der Titel des Wikipedia-Artikels als String
    """
    
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.lstrip('/').split('/')
    
    if len(path_parts) > 1 and path_parts[0] == "wiki":
        return unquote(path_parts[1].replace('_', ' '))
    
    return "Wikipedia-URL nicht auslesbar"


def link_list(list):

    """
    Extrahiert aus einer Liste von URLs die Überschriften
    
    param list: die zu analysierende URL-Liste
    return: Eine Liste aus den Titeln der URLs aus der eingegebenen Liste
    """
    
    li_ausgabe = []
    url_1 = ""
    url_2 = ""
    for i in range (len(list)):
        url_1 = str(list[i])
        url_2 = wikipedia_title(list[i])
    
        li_ausgabe = li_ausgabe + [url_2]
        
        
    return li_ausgabe

def counter(list,perfect_list):

    """
    Entwickelt eine Gesamtpunktzahl der Runde
    
    param list: Die Liste der aufgerufenen URLs
    param perfect_list: Liste des perfekten Wegs
    return: Gibt eine ganzzahlige Punktzahl zurück
    """
    
    p1 = len(list)
    pR = len(perfect_list)
    diff = p1 - pR

    points = 1.1 ** (- diff * (p1/pR)) * 10000
    return int(points)

def normal_counter (list):

    """
    Entwickelt eine Gesamtpunktzahl der Runde
    10.000 ist dabei die höchstmögliche Punktzahl
    
    param list: Die Liste der aufgerufenen URLs
    return: Gibt eine ganzzahlige Punktzahl zurück
    """
    
    p1 = len(list)
    points = 1.1 ** (- len(list) + 1) * 10000

    return int(points)

def list_as_str(list):

    """
    Gibt eine alternative Auflistung einer Liste wieder

    paaram list: die aufzulistene Liste
    return: Einen String, bestehend aus den Strings der eingegebenen Liste, nummeriert
    """
    
    str_1 = ""
    for i in range (len(list)):
        str_1 = str_1 + "\n" + str(i + 1) + ". "+ str(list[i])
    return str_1





"""

# Beispielaufrufe:

print(wikipedia_title("https://de.wikipedia.org/wiki/Python_(Programmiersprache)"))  # Gibt "Python (Programmiersprache)" zurück
print(wikipedia_title("https://en.wikipedia.org/wiki/Albert_Einstein"))  # Gibt "Albert Einstein" zurück
li_t = ["a","https://de.wikipedia.org/wiki/Benutzer:Julia_Gebert_(WMDE)","https://de.wikipedia.org/wiki/Python_(Programmiersprache)","Y","Y","WS","H","J"]
li_X = ["a","B","https://de.wikipedia.org/wiki/Python_(Programmiersprache",]
print(str(len(li_t)))
print(link_list(li_t))
print(str(counter (li_t, li_X)))
print(str(normal_counter(li_t)))
print(list_as_str(link_list(li_t)))


stoppuhr = Stoppuhr()
stoppuhr.start()
time.sleep(5)  # Simuliert eine Laufzeit von 5 Sekunden
stoppuhr.stop()
print(f"Gestoppte Zeit: {stoppuhr.get_zeit()} Sekunden")
print(random_Wiki_URL())

"""
