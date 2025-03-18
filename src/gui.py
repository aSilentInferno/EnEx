import webview
from enex_api import get_wiki_page


start = get_wiki_page("Wasserstoff") # noch keine zufällige Seite
# Python-Funktion, die von JavaScript aufgerufen wird
class Api:
    def __init__(self):
        self.last_clicked_url = None  # Variable zum Speichern der letzten geklickten URL
        
    def link_clicked(self, url):
        self.last_clicked_url = url  # Speichere die URL
        print(f"Link geklickt: {url}")  # Ausgabe der URL in der Konsole
        if url and url[0] == '.':
            link = get_wiki_page(url[2:])
        window.load_html(html_content.replace(start.inhalt, link.inhalt))  # Lade die URL im gleichen Fenster


script = """
<script>
    function handleLinkClick(event) {
        event.preventDefault(); // Verhindert das Standardverhalten des Links
        window.pywebview.api.link_clicked(event.target.href); // Ruft die Python-Funktion auf
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

# Erstelle ein Fenster mit dem HTML-Inhalt
window = webview.create_window('HTML Viewer', html=html_content, js_api=Api())

# Registriere die API für den Zugriff von JavaScript auf Python
webview.start()
