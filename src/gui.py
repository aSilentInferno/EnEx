import webview
from EnEx_API import get_wiki_inhalt
from wikipedia import Wikipedia


start = get_wiki_inhalt("Wasserstoff") # noch keine zufällige Seite

class Api:
    """
    Diese Klasse stellt eine API für die Kommunikation zwischen Python und JavaScript bereit.
    Sie ermöglicht das Verarbeiten von Klicks auf Links in der Webansicht.
    """
    def __init__(self):
        """
        Initialisiert die API-Klasse und setzt die Variable zum Speichern der letzten geklickten URL.
        """
        self.last_geklickt_url = None # Variable zum Speichern der letzten geklickten URL
        
    def link_geklickt(self, url): # Python-Funktion, die von JavaScript aufgerufen wird
        """
        Verarbeitet das Ereignis, wenn ein Link geklickt wird.
        
        Args:
            url (str): Die URL des geklickten Links.
        
        Returns:
            None: Gibt None zurück, wenn ein externer Link geklickt wird. Dadurch wird das Öffnen des Links verhindert.
        """
        self.last_geklickt_url = url  # Speichere die URL
        if url and url[0] == '.':
            url = url[2:]
        else:
            return None  # Wenn ein externer Link geklickt wird, wird das Öffnen des Links verhindert 
        print(f"Link geklickt: {url}")  # Ausgabe der URL in der Konsole - nur für Testzwecke! 
        link = get_wiki_inhalt(url)  # die URL kürzen, damit get_wiki_inhalt funktioniert
        window.load_html(html_content.replace(start.inhalt, link.inhalt))  # Lade die URL im gleichen Fenster


script = """
<script>
    function handleLinkClick(event) {
        event.preventDefault(); // Verhindert das Standardverhalten des Links
        window.pywebview.api.link_geklickt(event.target.href); // Ruft die Python-Funktion auf
    }

    // Fügt den Klick-Handler zu allen Links hinzu
    function addLinkHandlers() {
        var links = document.getElementsByTagName('a');
        for (var i = 0; i < links.length; i++) {
            links[i].onclick = handleLinkClick;
        }
    }

    // Füge die Link-Handler hinzu, wenn die Seite geladen wird
    window.onload = function() {
        addLinkHandlers();
    };
</script>
"""

# HTML-Inhalt mit Linkverarbeitung
html_content = """
<html>
<head>
    <style>
        h1 { color: #202122; }
        p { color: #333; }
    </style>
    """ + script + """
</head>
<body>
    """ + start.inhalt + """
</body>
</html>
"""

window = webview.create_window('HTML Viewer', html=html_content, js_api=Api())

webview.start()
