import os
import sys
import pyperclip
from PySide2 import QtWidgets, QtGui


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
    
        self.setToolTip(f'PathCopy')
        menu = QtWidgets.QMenu(parent)

        open_app = menu.addAction("cd /Users/georgesaker")
        open_app.triggered.connect(self.copyhome)

        open_cal = menu.addAction("cd /Users/georgesaker/Desktop")
        open_cal.triggered.connect(self.copydesktop)

        exit = menu.addAction("Quit")
        exit.triggered.connect(lambda: sys.exit())

        self.setContextMenu(menu)



    def copyhome(self):
        pyperclip.copy("cd /Users/georgesaker")

    def copydesktop(self):
        pyperclip.copy("cd /Users/georgesaker/Desktop")


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
