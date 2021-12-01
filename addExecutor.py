from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5.QtSql import QSqlTableModel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 769)
        MainWindow.setMinimumSize(QtCore.QSize(952, 769))
        MainWindow.setMaximumSize(QtCore.QSize(952, 769))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.executTable = QtWidgets.QTableView(self.centralwidget)
        self.executTable.setObjectName("executTable")
        self.verticalLayout.addWidget(self.executTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        # self.DelExecutBtn = QtWidgets.QPushButton(self.centralwidget)
        # self.DelExecutBtn.setObjectName("DelExecutBtn")
        # self.horizontalLayout.addWidget(self.DelExecutBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.create_table()
        # self.DelExecutBtn.clicked.connect(self.delete_from_table)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список исполнителей"))
        # self.DelExecutBtn.setText(_translate("MainWindow", "Удалить исполнителя"))

    def create_table(self):
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('TAH.db')
        con.open()
        stm = QtSql.QSqlTableModel()
        stm.setTable('Executors')
        stm.setSort(1, QtCore.Qt.AscendingOrder)
        stm.select()
        model = QtSql.QSqlQueryModel()
        model.setQuery("""SELECT Executor_ID, Executor_name, Languages, Cost_for_1800s, Order_ID FROM Executors""")
        model.setHeaderData(0, QtCore.Qt.Horizontal, '№/')
        model.setHeaderData(1, QtCore.Qt.Horizontal, 'Фамилия Имя')
        model.setHeaderData(2, QtCore.Qt.Horizontal, 'Языковая пара')
        model.setHeaderData(3, QtCore.Qt.Horizontal, 'Оплата за 1800 символов')
        model.setHeaderData(4, QtCore.Qt.Horizontal, 'Номер заказа')
        self.executTable.setModel(model)

    # def delete_from_table(self):
    #     con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    #     con.setDatabaseName('TAH.db')
    #     con.open()
    #     stm = QtSql.QSqlTableModel()
    #     stm.setTable('Executors')
    #     stm.setEditStrategy(QSqlTableModel.OnFieldChange)
    #     stm.setSort(1, QtCore.Qt.AscendingOrder)
    #     stm.select()
    #     indices = self.executTable.selectionModel().selectedRows()
    #     for index in sorted(indices):
    #         stm.removeRow(index.row())