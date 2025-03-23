import webview
from EnEx_API import get_wiki_inhalt, get_zufallige_seite
from wikipedia import Wikipedia



link = ""

history = []

class Api:
    """
    Diese Klasse stellt eine API für die Kommunikation zwischen Python und JavaScript bereit.
    Sie ermöglicht das Verarbeiten von Klicks auf Links in der Webansicht.
    """
    def __init__(self):
        """
        Initialisiert die API-Klasse und setzt die Variable zum Speichern der letzten geklickten URL.
        """
        self.zuletzt_geklickte_url = None # Variable zum Speichern der letzten geklickten URL

    def starte_Spiel(self, start, ziel):
        global link
        global script
        global html_content
        global history
        global wiki_window

        if start == "":
            start = get_zufallige_seite()
        if ziel == "":
            ziel = get_zufallige_seite()

        link = get_wiki_inhalt(start)
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
            """ + link.inhalt + """
        </body>
        </html>
        """
        history.append(start)
        wiki_window.load_html(html_content)
        
    def link_geklickt(self, url): # Python-Funktion, die von JavaScript aufgerufen wird
        """
        Verarbeitet das Ereignis, wenn ein Link geklickt wird.
        
        Args:
            url (str): Die URL des geklickten Links.
        
        Returns:
            None: Gibt None zurück, wenn ein externer Link geklickt wird. Dadurch wird das Öffnen des Links verhindert.
        """
        global history
        self.zuletzt_geklickte_url = url  # Speichere die URL
        if url.startswith("./"):
            history.append(url[2:])
            reload_link(url[2:])
        elif url.startswith("/wiki/"):
            history.append(url[6:])
            reload_link(url[6:])
        else:
            return None  # Wenn ein externer Link geklickt wird, wird das Öffnen des Links verhindert 
        
def reload_link(title): 
    global link
    global html_content
    global wiki_window
    global script
    link = get_wiki_inhalt(title)  # die URL kürzen, damit get_wiki_inhalt funktioniert
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
        """ + link.inhalt + """
    </body>
    </html>
    """
    wiki_window.load_html(html_content)  # Lade die URL im gleichen Fenster


script = ""

# HTML-Inhalt mit Linkverarbeitung
html_content = ""

menu_html = """
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enzyklopädie-Expedition</title>
    <script>
        function starteSpiel() {
            event.preventDefault();
            let start = ""; // Declare start and ziel outside the blocks
            let ziel = "";
            if (document.getElementById("startInput").value == "") {
                start = ""; // Random start article
            } else {
                start = document.getElementById("startInput").value;
            }
            if (document.getElementById("zielInput").value == "") {
                ziel = ""; // Random target article
            } else {
                ziel = document.getElementById("zielInput").value;
            }
            window.pywebview.api.starte_Spiel(start, ziel);
        }
    </script>
</head>
<body>
    <h1>Enzyklopädie-Expedition</h1>
    <button onclick="starteSpiel()">Starte das Spiel</button>
    <br><br>
    <p>Solltest du anstatt zufällig ausgewählter Start- und Zielseiten selber welche auswählen wollen, gib bitte unten die Titel dieser Seiten ein. </p>
    <input type="text" id = "startInput" placeholder="Titel für den Start" style="width: 300px;">
    <br><br>
    <input type="text" id = "zielInput" placeholder="Titel für das Ziel" style="width: 300px;">
</body>
</html>
"""

wiki_window = webview.create_window('HTML Viewer', html=html_content, js_api=Api())

menu_window = webview.create_window('Enzyklopädie-Expedition', html=menu_html, js_api=Api())




webview.start()