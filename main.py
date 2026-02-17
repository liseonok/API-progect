import sys
from PyQt6.QtWidgets import QApplication, QPushButton
from PyQt6.QtWidgets import QMainWindow


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

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

        self.btn = QLabel(self)
        self.btn.setText("Никакая")
        self.btn.move(30, 50)

    def mousePressEvent(self, event):
        self.coords.setText(f"Координаты:{event.pos().x()}, {event.pos().y()}")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())