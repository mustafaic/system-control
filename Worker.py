import os
import requests
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import ctypes
import socket


class Worker(QThread):
    update_signal = pyqtSignal(str, bool)

    def run(self):
        unc_path = r"\\b101ftp\paylasim"
        while True:
            self.check_site("internet","https://www.google.com")
            self.check_site("website", "https://bolge01.dsi.gov.tr/")
            self.check_site("belgenet", "https://belgenet.dsi.gov.tr/edys-web/sistemeGiris.xhtml")
            self.file_check(unc_path,"b101")


    def check_site(self, name, url):
        try:
            response = requests.get(url, timeout=5)
            result = response.status_code == 200

        except requests.RequestException:
            result = False

        self.update_signal.emit(name, result)


    def file_check(self, unc_path: str, name):
        result = False

        if os.path.exists(unc_path):
            print("UNC klasörüne erişim başarılı.")
            result = True

        self.update_signal.emit(name, result)