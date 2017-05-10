import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)
        menu = QtWidgets.QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(parent.close)
        self.setContextMenu(menu)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('TrayIcon Test')
        self.setWindowIcon(QtGui.QIcon('test.png'))
        self.tray_icon = SystemTrayIcon(QtGui.QIcon('test.png'), self)
        self.tray_icon.activated.connect(self.iconActivated)
        self.tray_icon.show()

        extractAction = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.show()

    def closeEvent(self, QCloseEvent):
        if self.tray_icon.isVisible():
            print("hiding...")
            self.hide()
            QCloseEvent.ignore()

    def iconActivated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.show()

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = Window()
    sys.exit(app.exec_())