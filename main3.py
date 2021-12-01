import sys
from PyQt5 import QtWidgets

import CreateOrder_new
import addExecutor
import addClient
from addClientInfo import Ui_MainWindow as Client_Main
from addExecutorInfo import Ui_MainWindow as Executor_Main
import Main


class MainWindow(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def open_win(self):
        self.addOrderBtn.clicked.connect(self.open)
        self.ClientsBtn.clicked.connect(self.open2)
        self.ExecutBtn.clicked.connect(self.open3)
        self.addClientBtn.clicked.connect(self.open4)
        self.addExecutBtn.clicked.connect(self.open5)

    def open(self):
        self.order = OrderWork()
        self.order.show()

    def open2(self):
        self.order2 = ClientWork()
        self.order2.show()

    def open3(self):
        self.order3 = ExecutorWork()
        self.order3.show()

    def open4(self):
        self.order4 = ClientInfo()
        self.order4.show()

    def open5(self):
        self.order5 = ExecutorInfo()
        self.order5.show()


class OrderWork(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super(OrderWork, self).__init__()
        self.ui2 = CreateOrder_new.Ui_MainWindow()
        self.ui2.setupUi(self)


class ClientWork(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super(ClientWork, self).__init__()
        self.ui3 = addClient.Ui_MainWindow()
        self.ui3.setupUi(self)


class ClientInfo(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super(ClientInfo, self).__init__()
        self.ui5 = Client_Main()
        self.ui5.setupUi(self)


class ExecutorInfo(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super(ExecutorInfo, self).__init__()
        self.ui6 = Executor_Main()
        self.ui6.setupUi(self)


class ExecutorWork(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super(ExecutorWork, self).__init__()
        self.ui4 = addExecutor.Ui_MainWindow()
        self.ui4.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.open_win()
    sys.exit(app.exec_())
