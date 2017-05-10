import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)
        menu = QtWidgets.QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(parent.close)
        self.setContextMenu(menu)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.tray_icon = SystemTrayIcon(QtGui.QIcon('test.png'), self)
        self.tray_icon.activated.connect(self.iconActivated)
        self.tray_icon.show()
        self.show()

    def closeEvent(self, QCloseEvent):
        if self.tray_icon.isVisible():
            print("hiding...")
            self.hide()
            QCloseEvent.ignore()

    def iconActivated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())