import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt


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

    def Page_Up(self, event):
        if event.key() == Qt.Key.Key_PageUp:
            pass

    def Page_Down(self, event):
        if event.key() == Qt.Key.Key_PageDown:
            pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())