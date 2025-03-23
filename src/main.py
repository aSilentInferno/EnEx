import EnEx_API
from gui import start_game
import optimalloesung


seitenHistorie = []
optimallösung = []
startseite = EnEx_API.get_wiki_inhalt(EnEx_API.get_zufällige_seite())
zielseite = EnEx_API.get_wiki_inhalt(EnEx_API.get_zufällige_seite())
def main():
    # starte das spiel fürs erste mal
    start_game()
    
def starte_runde():
    global startseite
    global zielseite
    global seitenHistorie
    global optimallösung
    
    seitenHistorie.append(startseite)
    optimallösung = optimalloesung.bidirektionale_breitensuche_wikipedia(startseite, zielseite)
    


if __name__ == "__main__":
    main()