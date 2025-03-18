## Autor: Clemens Stein
## Funktionen: Stoppuhr

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
