import EnEx_API
from gui import start_game
import optimalloesung


seitenHistorie = []
optimallösung = []
startseite = EnEx_API.get_wiki_inhalt(EnEx_API.get_zufällige_seite())
zielseite = EnEx_API.get_wiki_inhalt(EnEx_API.get_zufällige_seite())
def main():
    # starte das spiel fürs erste mal
    start_game(startseite, zielseite)
    
def starte_runde():
    global startseite
    global zielseite
    global seitenHistorie
    global optimallösung
    
    seitenHistorie.append(startseite)
    optimallösung = optimalloesung.bidirektionale_breitensuche_wikipedia(startseite, zielseite)

def neue_seite(link):
    global startseite
    global zielseite
    global seitenHistorie
    global optimallösung
    seitenHistorie.append(link)
    if(link == zielseite):
        # spiel gewonnen
        zeige_gewonnen(startseite, zielseite, seitenHistorie, optimallösung)
    else:
        # update momentane seite
        

if __name__ == "__main__":
    main()