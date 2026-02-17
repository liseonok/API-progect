import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtWidgets import QMainWindow
import requests


map_file = "map.png"


def get_card_by_coord_and_size(lan, lot, z=15, theme="light"):
    api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    url = "https://static-maps.yandex.ru/v1?"
    params = {
        "apikey": api_key,
        "ll": f'{lan},{lot}',
        "z": z,
        "theme": theme,
    }
    response = requests.get(url, params=params)
    if response:
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        print("Ошибка выполнения запроса:")
        print(url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None

lan = input()
lot = input()
z = int(input())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("API-project")
        self.setGeometry(0, 0, 1960, 1600)
        self.initUI()

    def initUI(self):
        self.style_button = QPushButton(self)
        self.style_button.move(40, 40)
        self.style_button.setText("Изменить тему")
        get_card_by_coord_and_size(lan, lot, z)
        self.image = QPixmap('map.png')
        self.label = QLabel(self)
        self.label.move(80, 60)
        self.label.resize(600, 450)
        self.label.setPixmap(self.image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())