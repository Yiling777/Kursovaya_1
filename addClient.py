from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlTableModel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 774)
        MainWindow.setMinimumSize(QtCore.QSize(1010, 774))
        MainWindow.setMaximumSize(QtCore.QSize(1010, 774))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clientTable = QtWidgets.QTableView(self.centralwidget)
        self.clientTable.setObjectName("clientTable")
        self.verticalLayout.addWidget(self.clientTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        # self.DelClientBtn = QtWidgets.QPushButton(self.centralwidget)
        # self.DelClientBtn.setObjectName("DelClientBtn")
        # self.horizontalLayout.addWidget(self.DelClientBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.create_table()
        # self.DelClientBtn.clicked.connect(self.delete_from_table)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список клиентов"))
        # self.DelClientBtn.setText(_translate("MainWindow", "Удалить клиента"))

    def create_table(self):
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('TAH.db')
        con.open()
        stm = QtSql.QSqlTableModel()
        stm.setTable('Customers')
        stm.setEditStrategy(QSqlTableModel.OnFieldChange)
        stm.setSort(1, QtCore.Qt.AscendingOrder)
        stm.select()
        model = QtSql.QSqlQueryModel()
        model.setQuery(
            """SELECT Cust_ID, Cust_name, Cust_phone_number, Cust_email, Cust_org_name, Order_ID FROM Customers""")
        model.setHeaderData(0, QtCore.Qt.Horizontal, '№/')
        model.setHeaderData(1, QtCore.Qt.Horizontal, 'Фамилия Имя')
        model.setHeaderData(2, QtCore.Qt.Horizontal, 'Контактный телефон')
        model.setHeaderData(3, QtCore.Qt.Horizontal, 'Электронная почта')
        model.setHeaderData(4, QtCore.Qt.Horizontal, 'Организация')
        model.setHeaderData(5, QtCore.Qt.Horizontal, 'Номер заказа')
        model.__sizeof__()
        self.clientTable.setModel(model)

    # def delete_from_table(self):
    #     con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    #     con.setDatabaseName('TAH.db')
    #     con.open()
    #     stm = QtSql.QSqlTableModel()
    #     stm.setTable('Customers')
    #     stm.setEditStrategy(QSqlTableModel.OnFieldChange)
    #     stm.setSort(1, QtCore.Qt.AscendingOrder)
    #     stm.select()
    #     indices = self.clientTable.selectionModel().selectedRows()
    #     for index in sorted(indices):
    #         stm.removeRow(index.row())
    #
    #     stm.select()
