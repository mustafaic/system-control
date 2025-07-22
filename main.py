import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import images_rc
import webbrowser
from Worker import Worker
from datetime import datetime


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.time = datetime.now()

        uic.loadUi("test1.ui", self)
        self.setWindowTitle("Sistem Kontrol")

        self.worker = Worker()
        self.worker.update_signal.connect(self.update_ui)
        self.worker.start()

        self.google_git.clicked.connect(lambda: self.link_ac("https://www.google.com/"))
        self.b101_button.clicked.connect(lambda: self.link_ac("https://www.youtube.com/"))
        self.belgenet_button.clicked.connect(lambda: self.link_ac("https://belgenet.dsi.gov.tr/edys-web/sistemeGiris.xhtml"))
        self.website_button.clicked.connect(lambda: self.link_ac("https://bolge01.dsi.gov.tr/"))


    def link_ac(self, url):
        webbrowser.open(url)


    @pyqtSlot(str, bool)
    def update_ui(self, site, status):
        if site == "internet":
            if status:
                self.internet_card.setStyleSheet("#internet_card {\n"
                                      "    border: 10px solid rgb(46, 204, 113);\n"
                                      "    border-radius: 70px;\n"
                                      "    padding: 10px;\n"
                                      "}")

                self.internet_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.internet_durum.setText("Durum: Çalışıyor")

            else:
                self.internet_card.setStyleSheet("#internet_card {\n"
                                                 "    border: 10px solid red;\n"
                                                 "    border-radius: 70px;\n"
                                                 "    padding: 10px;\n"
                                                 "}")

                self.internet_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.internet_durum.setText("Durum: Çalışmıyor")


        elif site == "website":
            if status:
                self.website_card.setStyleSheet("#website_card {\n"
                                      "    border: 10px solid rgb(46, 204, 113);\n"
                                      "    border-radius: 70px;\n"
                                      "    padding: 10px;\n"
                                      "}")

                self.website_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.website_durum.setText("Durum: Çalışıyor")

            else:
                self.website_card.setStyleSheet("#website_card {\n"
                                                "    border: 10px solid red;\n"
                                                "    border-radius: 70px;\n"
                                                "    padding: 10px;\n"
                                                "}")

                self.website_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.website_durum.setText("Durum: Çalışmıyor")


        elif site == "belgenet":
            if status:
                self.belgenet_card.setStyleSheet("#belgenet_card {\n"
                                      "    border: 10px solid rgb(46, 204, 113);\n"
                                      "    border-radius: 70px;\n"
                                      "    padding: 10px;\n"
                                      "}")

                self.belgenet_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.belgenet_durum.setText("Durum: Çalışıyor")

            else:
                self.belgenet_card.setStyleSheet("#belgenet_card {\n"
                                                 "    border: 10px solid red;\n"
                                                 "    border-radius: 70px;\n"
                                                 "    padding: 10px;\n"
                                                 "}")

                self.belgenet_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.belgenet_durum.setText("Durum: Çalışmıyor")


        elif site == "b101":
            if status:
                self.b101_card.setStyleSheet("#b101_card {\n"
                                      "    border: 10px solid rgb(46, 204, 113);\n"
                                      "    border-radius: 70px;\n"
                                      "    padding: 10px;\n"
                                      "}")

                self.b101_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.b101_durum.setText("Durum: Çalışıyor")

            else:
                self.b101_card.setStyleSheet("#b101_card {\n"
                                             "    border: 10px solid red;\n"
                                             "    border-radius: 70px;\n"
                                             "    padding: 10px;\n"
                                             "}")

                self.b101_check.setText(datetime.now().strftime("%H:%M:%S"))
                self.b101_durum.setText("Durum: Çalışmıyor")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
