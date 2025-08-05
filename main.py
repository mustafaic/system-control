import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import images_rc
import webbrowser
from Worker import Worker
from datetime import datetime
from test1 import Ui_MainWindow
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.time = datetime.now()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(resource_path("test.ico")))

        self.setWindowTitle("Sistem Kontrol")

        self.worker = Worker()
        self.worker.update_signal.connect(self.update_ui)
        self.worker.start()

        self.ui.google_git.clicked.connect(lambda: self.link_ac("https://www.google.com/"))
        self.ui.b101_button.clicked.connect(lambda: self.link_ac("https://www.youtube.com/"))
        self.ui.belgenet_button.clicked.connect(lambda: self.link_ac("https://belgenet.dsi.gov.tr/edys-web/sistemeGiris.xhtml"))
        self.ui.website_button.clicked.connect(lambda: self.link_ac("https://bolge01.dsi.gov.tr/"))


    def startMaximized(self):
        self.showMaximized()


    def link_ac(self, url):
        webbrowser.open(url)


    @pyqtSlot(str, bool)
    def update_ui(self, site, status):
        if site == "internet":
            if status:
                self.ui.internet_card.setStyleSheet("#internet_card {\n"
                                      "    border: 10px solid rgb(46, 204, 113);\n"
                                      "    border-radius: 70px;\n"
                                      "    padding: 10px;\n"
                                      "}")

                self.ui.internet_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.ui.internet_durum.setText("Durum: Çalışıyor")

            else:
                self.ui.internet_card.setStyleSheet("#internet_card {\n"
                                                 "    border: 10px solid red;\n"
                                                 "    border-radius: 70px;\n"
                                                 "    padding: 10px;\n"
                                                 "}")

                self.ui.internet_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.ui.internet_durum.setText("Durum: Çalışmıyor")


        elif site == "website":
            if status:
                self.ui.website_card.setStyleSheet("#website_card {\n"
                                      "    border: 10px solid rgb(46, 204, 113);\n"
                                      "    border-radius: 70px;\n"
                                      "    padding: 10px;\n"
                                      "}")

                self.ui.website_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.ui.website_durum.setText("Durum: Çalışıyor")

            else:
                self.ui.website_card.setStyleSheet("#website_card {\n"
                                                "    border: 10px solid red;\n"
                                                "    border-radius: 70px;\n"
                                                "    padding: 10px;\n"
                                                "}")

                self.ui.website_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.ui.website_durum.setText("Durum: Çalışmıyor")


        elif site == "belgenet":
            if status:
                self.ui.belgenet_card.setStyleSheet("#belgenet_card {\n"
                                      "    border: 10px solid rgb(46, 204, 113);\n"
                                      "    border-radius: 70px;\n"
                                      "    padding: 10px;\n"
                                      "}")

                self.ui.belgenet_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.ui.belgenet_durum.setText("Durum: Çalışıyor")

            else:
                self.ui.belgenet_card.setStyleSheet("#belgenet_card {\n"
                                                 "    border: 10px solid red;\n"
                                                 "    border-radius: 70px;\n"
                                                 "    padding: 10px;\n"
                                                 "}")

                self.ui.belgenet_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.ui.belgenet_durum.setText("Durum: Çalışmıyor")


        elif site == "b101":
            if status:
                self.ui.b101_card.setStyleSheet("#b101_card {\n"
                                      "    border: 10px solid rgb(46, 204, 113);\n"
                                      "    border-radius: 70px;\n"
                                      "    padding: 10px;\n"
                                      "}")

                self.ui.b101_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.ui.b101_durum.setText("Durum: Çalışıyor")

            else:
                self.ui.b101_card.setStyleSheet("#b101_card {\n"
                                             "    border: 10px solid red;\n"
                                             "    border-radius: 70px;\n"
                                             "    padding: 10px;\n"
                                             "}")

                self.ui.b101_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.ui.b101_durum.setText("Durum: Çalışmıyor")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.startMaximized()
    sys.exit(app.exec_())
