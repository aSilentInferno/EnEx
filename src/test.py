import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QUrl

import EnEx_API

class HTMLViewer(QMainWindow):
    def __init__(self, history):
        super().__init__()
        self.history = history
        self.initUI()

    def initUI(self):
        self.setWindowTitle('HTML Viewer')
        self.setGeometry(100, 100, 800, 600)

        # Create a QTextBrowser widget
        self.textBrowser = QTextBrowser()
        self.textBrowser.setOpenExternalLinks(False)  # Disable opening links in an external browser
        self.textBrowser.anchorClicked.connect(self.handle_link_click)  # Connect the signal to the slot

        # Create a QPushButton widget
        self.button = QPushButton('Load Random Page')
        self.button.clicked.connect(self.load_random_page)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.textBrowser)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def set_html_content(self, html_content):
        self.textBrowser.setHtml(html_content)

    def load_random_page(self):
        # Placeholder function to be executed when the button is pressed
        new_content = EnEx_API.get_wiki_inhalt(EnEx_API.get_zufallige_seite()).inhalt
        self.set_html_content(new_content)
        self.history.append(new_content)  # Update the history variable

    def handle_link_click(self, url):
        # Handle the link click event
        print(f"Link clicked: {url.toString()}")
        # You can load the content of the clicked link here
        # For example, you can fetch the content from the URL and display it in the text browser
        # new_content = fetch_content_from_url(url.toString())
        # self.set_html_content(new_content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = HTMLViewer([])
    viewer.show()
    sys.exit(app.exec_())