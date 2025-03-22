from collections import deque
import time
from wikipedia import Wikipedia
from EnEx_API import get_wiki_links

FOR = "forwärts"
RÜCK = "zurück"

def bidirektionale_breitensuche_wikipedia(start, ziel):
    """
    Findet den kürzesten Pfad zwischen zwei Wikipedia-Seiten mittels bidirektionaler Breitensuche. (BFS)
    auswahl des Suchalgorithmus basierend auf den fünden aus https://www2.informatik.uni-stuttgart.de/bibliothek/ftp/medoc.ustuttgart_fi/DIP-3410/DIP-3410.pdf
    :param start: Der name der Startseite
    :param ziel: Der name der Zielseite
    :return: Die Liste der Seiten, die den kürzesten Pfad zwischen den beiden Seiten darstellen.
    """
    if start == ziel:
        return [start]

    vorwärts_warteschlange = deque([(start, [start])])
    rückwärts_warteschlange = deque([(ziel, [ziel])])

    forwärts_besucht = {start: [start]}
    rückwärts_besucht = {ziel: [ziel]}

    while vorwärts_warteschlange and rückwärts_warteschlange:
        # Die kleine Anzahl von Schritten wird zuerst durchgeführt, um die Anzahl der Schritte zu minimieren
        if len(vorwärts_warteschlange) <= len(rückwärts_warteschlange):
            ergebnis = _erweitere_suchweite(vorwärts_warteschlange, forwärts_besucht, rückwärts_besucht, richtung=FOR)
        else:
            ergebnis = _erweitere_suchweite(rückwärts_warteschlange, rückwärts_besucht, forwärts_besucht, richtung=RÜCK)

        if ergebnis:
            return ergebnis
    # falls keine Lösung gefunden wurde und alle links abgesucht wurden
    return None

def _erweitere_suchweite(warteschlange, bereits_besucht, andere_seite_besucht, richtung):
    """
    Erweitert die Suchwarteschlange, indem Wikipedia-Objekte abgerufen und deren Links überprüft werden.
    :param queue: Die Warteschlange, die erweitert werden soll.
    :param visited: Das besuchte Dictionary für diese Richtung.
    :param other_visited: Das besuchte Dictionary der entgegengesetzten Richtung.
    :param direction: "forwärts" für ausgehende Links, "rückwärts" für eingehende Links.
    :return: Der kürzeste Pfad, wenn gefunden, andernfalls None.
    """
    for _ in range(len(warteschlange)):
        aktuell, pfad = warteschlange.popleft()
        wiki_seite = get_wiki_links(aktuell)
        
        ausgehende_seiten = wiki_seite.ausgehende_links if richtung == FOR else wiki_seite.eingehende_links

        for seite in ausgehende_seiten:
            if seite in bereits_besucht:
                continue

            erweiterter_pfad = pfad + [seite] if richtung == FOR else [seite] + pfad
            bereits_besucht[seite] = erweiterter_pfad

            if seite in andere_seite_besucht:  # Wenn Seiten in beiden Richtungen gefunden wurden, gibt es eine Lösung
                return _vereinige_pfade(erweiterter_pfad, andere_seite_besucht[seite],richtung)

            warteschlange.append((seite, erweiterter_pfad))

        time.sleep(0.5)  # Verhindere Unnötige Anfragen an die Wikipedia-API

    return None

def _vereinige_pfade(erweiterter_pfad, umgekehrter_pfad, richtung):
    """ Fügt die Beiden Pfade zusammen. """
    if richtung == FOR:
        return erweiterter_pfad + umgekehrter_pfad[1:]
    else:
        return umgekehrter_pfad + erweiterter_pfad[1:]