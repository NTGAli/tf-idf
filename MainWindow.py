import os
from threading import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  #QIcon
from PyQt5.QtWebEngineWidgets import *
import sys

import br



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(f'file:///{getPathOfHtml()}/helloworld.html'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        nav = QToolBar()
        # set icon size
        nav.setIconSize(QSize(24,24))
        self.addToolBar(nav)

        # navigation toolbar
        home_btn = QAction(QIcon("assets/home.png"),'Click to open Home page', self)
        home_btn.triggered.connect(self.home)
        nav.addAction(home_btn)
        back_btn = QAction(QIcon("assets/back.png"),'Click to go back', self)
        back_btn.triggered.connect(self.browser.back)
        nav.addAction(back_btn)
        forward_btn = QAction(QIcon("assets/forward.png"),'Click to go forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        nav.addAction(forward_btn)
        reload_btn = QAction(QIcon("assets/refresh.png"),'Click to Refresh this page', self)
        reload_btn.triggered.connect(self.browser.reload)
        nav.addAction(reload_btn)

        self.url_entry = QLineEdit()
        self.url_entry.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.url_entry)
        self.browser.urlChanged.connect(self.update_url)
    def home(self):
        # set home url
        self.browser.setUrl(QUrl(f'file:///{getPathOfHtml()}/helloworld.html'))
    def navigate_to_url(self):
        self.NTU()

    def update_url(self, entered_url):
        # update url to entry widget
        global query
        self.url_entry.setText(entered_url.toString())

    def NTU(self):
        # # get url
        url = self.url_entry.text()
        # # set url
        self.browser.setUrl(QUrl(url))
        global query
        # t1 = threading.Thread(target=print_square, args=(10,))
        if self.url_entry.text() != "about:blank" and self.url_entry.text() is not None:
            print(self.url_entry.text())
            query = self.url_entry.text()
            br.makeHtml(query)
            self.browser.setUrl(QUrl(f'file:///{getPathOfHtml()}/helloworld.html'))


def getPathOfHtml():
    ROOT_DIR = os.path.dirname(os.path.abspath("helloworld.html"))
    print(ROOT_DIR.replace('\\', '/'))
    return ROOT_DIR.replace('\\', '/')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Browser')
    window = MainWindow()
    app.exec_()
