import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QMainWindow
import requests


map_file = "map.png"
MASHTAB = 15
THEME = "light"


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
        self.setGeometry(0, 0, 700, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        get_card_by_coord_and_size(lan, lot, z)
        self.image = QPixmap('map.png')
        self.label = QLabel(self)
        self.label.move(80, 60)
        self.label.resize(600, 450)
        self.label.setPixmap(self.image)

        self.style_button = QPushButton(self)
        # self.style_button.move(40, 40)
        layout.addWidget(self.style_button)
        self.style_button.setText("Изменить тему")
        self.pg_up_button = QPushButton(self)
        self.pg_up_button.setText("Увеличить")
        layout.addWidget(self.pg_up_button)
        self.pg_up_button.clicked.connect(self.pg_up_button_clicked)
        self.pg_down_button = QPushButton(self)
        self.pg_down_button.setText("Уменьшить")
        layout.addWidget(self.pg_down_button)
        self.pg_down_button.clicked.connect(self.pg_down_button_clicked)

        layout.addWidget(self.label)

    def pg_up_button_clicked(self):
        global MASHTAB, THEME
        if MASHTAB < 21:
            MASHTAB += 1
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def pg_down_button_clicked(self):
        global MASHTAB, THEME
        if MASHTAB > 1:
            MASHTAB -= 1
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    55.753544, 37.621202