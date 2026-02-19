import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit
from PyQt6.QtWidgets import QMainWindow
import requests


map_file = "map.png"
MASHTAB = 15
THEME = "light"
ADDRESS = ''
lan = '37.621202'
lot = '55.753544'
z = 15
lanpt = lan
lotpt = lot
point_needed = True


def update_pt(lan, lot):
    global lanpt, lotpt
    lanpt = lan
    lotpt = lot


def get_coord_by_address(address):
    params = {
        "apikey": '4ac3ce67-d2de-4ba8-87c8-c5443f4d8776',
        "geocode": address,
        "format": "json"}
    response = requests.get('http://geocode-maps.yandex.ru/1.x/?', params=params)
    if response:
        response1 = response.json()
        toponym = response1["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        lan, lot = toponym_coodrinates.split()
        return float(lot), float(lan)
    else:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None



def get_card_by_coord_and_size(lan, lot, z=15, theme="light", lanpt1=lanpt, lotpt1=lotpt):
    api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    url = "https://static-maps.yandex.ru/v1?"
    print(lanpt1, lotpt1)
    print(lan, lot)
    if point_needed:
        params = {
            "apikey": api_key,
            "ll": f'{lan},{lot}',
            "z": z,
            "theme": theme,
            "pt": f'{lanpt1},{lotpt1},pm2pnl'
        }
    else:
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


lan = '37.621202'
lot = '55.753544'
z = 15

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

        self.adress_input = QLineEdit(self)
        self.adress_input_button = QPushButton(self)
        self.adress_input_button.setText('Ввести')
        self.adress_input_button.clicked.connect(self.import_adress)

        self.cancel_button = QPushButton(self)
        self.cancel_button.setText("Отменить")
        self.cancel_button.clicked.connect(self.cancel)

        hlayout = QHBoxLayout()
        self.left_button = QPushButton(self)
        self.left_button.setText("Влево")
        self.left_button.clicked.connect(self.left)
        self.right_button = QPushButton(self)
        self.right_button.setText("Вправо")
        self.right_button.clicked.connect(self.right)
        self.up_button = QPushButton(self)
        self.up_button.setText("Вверх")
        self.up_button.clicked.connect(self.up)
        self.down_button = QPushButton(self)
        self.down_button.setText("Вниз")
        self.down_button.clicked.connect(self.down)
        hlayout.addWidget(self.left_button)
        hlayout.addWidget(self.right_button)
        hlayout.addWidget(self.up_button)
        hlayout.addWidget(self.down_button)

        self.style_button = QPushButton(self)
        # self.style_button.move(40, 40)
        layout.addWidget(self.style_button)
        self.style_button.setText("Изменить тему")
        self.style_button.clicked.connect(self.change_theme)
        self.pg_up_button = QPushButton(self)
        self.pg_up_button.setText("Увеличить")
        layout.addWidget(self.pg_up_button)
        self.pg_up_button.clicked.connect(self.pg_up_button_clicked)
        self.pg_down_button = QPushButton(self)
        self.pg_down_button.setText("Уменьшить")
        layout.addWidget(self.pg_down_button)
        self.pg_down_button.clicked.connect(self.pg_down_button_clicked)

        layout.addWidget(self.adress_input)
        layout.addWidget(self.adress_input_button)
        layout.addWidget(self.cancel_button)
        layout.addLayout(hlayout)


        layout.addWidget(self.label)

    def cancel(self):
        global point_needed
        point_needed = False
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def pg_up_button_clicked(self):
        global MASHTAB, THEME
        if MASHTAB < 21:
            MASHTAB += 1
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def pg_down_button_clicked(self):
        global MASHTAB, THEME
        if MASHTAB > 1:
            MASHTAB -= 1
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def right(self):
        global lan, MASHTAB, THEME
        lan = str(float(lan) + 0.0008)
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def left(self):
        global lan, MASHTAB, THEME
        lan = str(float(lan) - 0.0008)
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def up(self):
        global lot, MASHTAB, THEME
        lot = str(float(lot) + 0.0008)
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def down(self):
        global lot, MASHTAB, THEME
        lot = str(float(lot) - 0.0008)
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def change_theme(self):
        global MASHTAB, THEME
        if THEME == "light":
            THEME = "dark"
        else:
            THEME = "light"
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)

    def import_adress(self):
        global lan, lot, z, MASHTAB, THEME, point_needed, lanpt, lotpt
        address = self.adress_input.text()
        if not address:
            return None
        lon, lat = get_coord_by_address(address)
        if not lat or not lon:
            return None
        lan, lot = lat, lon
        update_pt(lan, lot)
        point_needed = True
        get_card_by_coord_and_size(lan, lot, MASHTAB, THEME, lanpt, lotpt)
        self.image = QPixmap('map.png')
        self.label.setPixmap(self.image)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    55.753544, 37.621202