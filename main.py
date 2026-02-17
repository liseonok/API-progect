import sys
from PyQt6.QtWidgets import QApplication, QPushButton
from PyQt6.QtWidgets import QMainWindow
import requests



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




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def get_card_by_coord_and_size(lan, lot, z):
    api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    url = "https://static-maps.yandex.ru/v1?"
    params = {
        "apikey": api_key,
        "ll": f'{lan},{lot}',
        "z": z
    }
    response = requests.get(url, params=params)
    if response:
        return response
    else:
        print("Ошибка выполнения запроса:")
        print(url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None