import sys
from PyQt5.QtWidgets import QApplication
import EnEx_API
from test import HTMLViewer

def main():
    history = [EnEx_API.get_wiki_inhalt(EnEx_API.get_zufallige_seite()).inhalt]
    app = QApplication(sys.argv)
    viewer = HTMLViewer(history)
    viewer.set_html_content(history[-1])
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()