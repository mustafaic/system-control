import requests
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import time


class Worker(QThread):
    update_signal = pyqtSignal(str, bool)

    def run(self):
        while True:
            self.check_site("internet","https://www.google.com")
            self.check_site("website", "https://bolge01.dsi.gov.tr/")
            self.check_site("belgenet", "https://belgenet.dsi.gov.tr/edys-web/sistemeGiris.xhtml")
            self.check_site("b101", "https://youtube.com/")


    def check_site(self, name, url):
        try:
            response = requests.get(url, timeout=5)
            result = response.status_code == 200

        except requests.RequestException:
            result = False

        self.update_signal.emit(name, result)

