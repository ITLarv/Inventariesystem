# Other py files
import util
import buttons
import database
import gui_update_functions

# Other dependencies
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def __init__(self):
		self.db = database.Mydatabase()
		self.gui_func = gui_update_functions.Gui_functions(self)

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		#MainWindow.resize(783, 584)
		MainWindow.setFixedSize(783, 584)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../images/logo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 781, 561))
		font = QtGui.QFont()
		font.setFamily("Arial")
		self.tabWidget.setFont(font)
		self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
		self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.tabWidget.setUsesScrollButtons(True)
		self.tabWidget.setObjectName("tabWidget")
		self.tab_storage = QtWidgets.QWidget()
		self.tab_storage.setObjectName("tab_storage")
		self.label_2 = QtWidgets.QLabel(self.tab_storage)
		self.label_2.setGeometry(QtCore.QRect(620, 430, 151, 161))
		self.label_2.setText("")
		self.label_2.setPixmap(QtGui.QPixmap("../images/logga-fyrkant.png"))
		self.label_2.setScaledContents(True)
		self.label_2.setObjectName("label_2")
		self.button_storage_search = QtWidgets.QPushButton(self.tab_storage)
		self.button_storage_search.setGeometry(QtCore.QRect(320, 80, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_storage_search.setFont(font)
		self.button_storage_search.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_storage_search.setObjectName("button_storage_search")
		self.label_6 = QtWidgets.QLabel(self.tab_storage)
		self.label_6.setGeometry(QtCore.QRect(30, 20, 221, 51))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.line_3 = QtWidgets.QFrame(self.tab_storage)
		self.line_3.setGeometry(QtCore.QRect(453, 0, 20, 511))
		self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.label_7 = QtWidgets.QLabel(self.tab_storage)
		self.label_7.setGeometry(QtCore.QRect(530, 20, 201, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.label_7.setFont(font)
		self.label_7.setObjectName("label_7")

		## Autocompleter companies setup ##
		completer_companies = QtWidgets.QCompleter(util.all_companies())
		completer_companies.setCaseSensitivity(0)

		completer_storageid = QtWidgets.QCompleter(util.all_storageid())
		completer_storageid.setCaseSensitivity(0)

		completer_companies_registerd = QtWidgets.QCompleter(util.all_registered_companies(self.db))
		completer_companies_registerd.setCaseSensitivity(0)


		self.lineEdit_storage_name = QtWidgets.QLineEdit(self.tab_storage)
		self.lineEdit_storage_name.setGeometry(QtCore.QRect(480, 70, 291, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.lineEdit_storage_name.setFont(font)
		self.lineEdit_storage_name.setObjectName("lineEdit_storage_name")
		self.lineEdit_storage_name.setCompleter(completer_companies_registerd)
		self.lineEdit_storage_borrow_id = QtWidgets.QLineEdit(self.tab_storage)
		self.lineEdit_storage_borrow_id.setGeometry(QtCore.QRect(480, 130, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.lineEdit_storage_borrow_id.setFont(font)
		self.lineEdit_storage_borrow_id.setObjectName("lineEdit_storage_borrow_id")
		self.button_storage_borrow = QtWidgets.QPushButton(self.tab_storage)
		self.button_storage_borrow.setGeometry(QtCore.QRect(650, 130, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_storage_borrow.setFont(font)
		self.button_storage_borrow.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_storage_borrow.setObjectName("button_storage_borrow")
		self.line_4 = QtWidgets.QFrame(self.tab_storage)
		self.line_4.setGeometry(QtCore.QRect(470, 240, 301, 20))
		self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.label_8 = QtWidgets.QLabel(self.tab_storage)
		self.label_8.setGeometry(QtCore.QRect(520, 270, 201, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.label_8.setFont(font)
		self.label_8.setObjectName("label_8")
		self.lineEdit_storage_return_id = QtWidgets.QLineEdit(self.tab_storage)
		self.lineEdit_storage_return_id.setGeometry(QtCore.QRect(480, 340, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.lineEdit_storage_return_id.setFont(font)
		self.lineEdit_storage_return_id.setObjectName("lineEdit_storage_return_id")
		self.button_storage_return = QtWidgets.QPushButton(self.tab_storage)
		self.button_storage_return.setGeometry(QtCore.QRect(650, 340, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_storage_return.setFont(font)
		self.button_storage_return.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_storage_return.setObjectName("button_storage_return")
		self.button_storage_checkin = QtWidgets.QPushButton(self.tab_storage)
		self.button_storage_checkin.setGeometry(QtCore.QRect(30, 370, 136, 91))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_storage_checkin.setFont(font)
		self.button_storage_checkin.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 20px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_storage_checkin.setObjectName("button_storage_checkin")
		self.button_storage_checkout = QtWidgets.QPushButton(self.tab_storage)
		self.button_storage_checkout.setGeometry(QtCore.QRect(280, 370, 141, 91))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_storage_checkout.setFont(font)
		self.button_storage_checkout.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 20px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_storage_checkout.setObjectName("button_storage_checkout")
		self.textBrowser_storage = QtWidgets.QTextBrowser(self.tab_storage)
		self.textBrowser_storage.setGeometry(QtCore.QRect(30, 150, 411, 150))
		self.textBrowser_storage.setObjectName("textBrowser_storage")
		self.button_storage_update = QtWidgets.QPushButton(self.tab_storage)
		self.button_storage_update.setGeometry(QtCore.QRect(320, 40, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_storage_update.setFont(font)
		self.button_storage_update.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_storage_update.setObjectName("button_storage_update")
		self.lineEdit_storage_company = QtWidgets.QLineEdit(self.tab_storage)
		self.lineEdit_storage_company.setGeometry(QtCore.QRect(30, 80, 281, 31))
		self.lineEdit_storage_company.setCompleter(completer_companies_registerd)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.lineEdit_storage_company.setFont(font)
		self.lineEdit_storage_company.setText("")
		self.lineEdit_storage_company.setClearButtonEnabled(False)
		self.lineEdit_storage_company.setObjectName("lineEdit_storage_company")
		self.tabWidget.addTab(self.tab_storage, "")
		self.tab_transportation = QtWidgets.QWidget()
		self.tab_transportation.setObjectName("tab_transportation")
		self.label_15 = QtWidgets.QLabel(self.tab_transportation)
		self.label_15.setGeometry(QtCore.QRect(620, 430, 151, 161))
		self.label_15.setText("")
		self.label_15.setPixmap(QtGui.QPixmap("../images/logga-fyrkant.png"))
		self.label_15.setScaledContents(True)
		self.label_15.setObjectName("label_15")
		self.label_10 = QtWidgets.QLabel(self.tab_transportation)
		self.label_10.setGeometry(QtCore.QRect(330, -10, 131, 51))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		self.label_10.setFont(font)
		self.label_10.setObjectName("label_10")
		self.lineEdit_transportation_company = QtWidgets.QLineEdit(self.tab_transportation)
		self.lineEdit_transportation_company.setGeometry(QtCore.QRect(130, 40, 321, 31))
		self.lineEdit_transportation_company.setCompleter(completer_companies)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.lineEdit_transportation_company.setFont(font)
		self.lineEdit_transportation_company.setText("")
		self.lineEdit_transportation_company.setClearButtonEnabled(False)
		self.lineEdit_transportation_company.setObjectName("lineEdit_transportation_company")
		self.textBrowser_transportation = QtWidgets.QTextBrowser(self.tab_transportation)
		self.textBrowser_transportation.setGeometry(QtCore.QRect(150, 80, 450, 151))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.textBrowser_transportation.setFont(font)
		self.textBrowser_transportation.setObjectName("textBrowser_transportation")
		self.button_transportation_search = QtWidgets.QPushButton(self.tab_transportation)
		self.button_transportation_search.setGeometry(QtCore.QRect(460, 40, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_transportation_search.setFont(font)
		self.button_transportation_search.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_transportation_search.setObjectName("button_transportation_search")
		self.line_9 = QtWidgets.QFrame(self.tab_transportation)
		self.line_9.setGeometry(QtCore.QRect(0, 240, 781, 16))
		self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.line_10 = QtWidgets.QFrame(self.tab_transportation)
		self.line_10.setGeometry(QtCore.QRect(370, 250, 41, 271))
		self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_10.setObjectName("line_10")
		self.label_16 = QtWidgets.QLabel(self.tab_transportation)
		self.label_16.setGeometry(QtCore.QRect(90, 250, 191, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.label_16.setFont(font)
		self.label_16.setObjectName("label_16")
		self.button_transportation_register = QtWidgets.QPushButton(self.tab_transportation)
		self.button_transportation_register.setGeometry(QtCore.QRect(80, 410, 201, 81))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_transportation_register.setFont(font)
		self.button_transportation_register.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 20px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_transportation_register.setObjectName("button_transportation_register")
		self.lineEdit_transportation_id = QtWidgets.QLineEdit(self.tab_transportation)
		self.lineEdit_transportation_id.setGeometry(QtCore.QRect(60, 320, 271, 31))
		self.lineEdit_transportation_id.setCompleter(completer_storageid)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.lineEdit_transportation_id.setFont(font)
		self.lineEdit_transportation_id.setText("")
		self.lineEdit_transportation_id.setClearButtonEnabled(False)
		self.lineEdit_transportation_id.setObjectName("lineEdit_transportation_id")
		self.button_transportation_send = QtWidgets.QPushButton(self.tab_transportation)
		self.button_transportation_send.setGeometry(QtCore.QRect(480, 410, 221, 81))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_transportation_send.setFont(font)
		self.button_transportation_send.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 20px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_transportation_send.setObjectName("button_transportation_send")
		self.line_11 = QtWidgets.QFrame(self.tab_transportation)
		self.line_11.setGeometry(QtCore.QRect(390, 380, 381, 16))
		self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_11.setObjectName("line_11")
		self.button_transportation_kollin_add = QtWidgets.QPushButton(self.tab_transportation)
		self.button_transportation_kollin_add.setGeometry(QtCore.QRect(440, 300, 101, 51))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_transportation_kollin_add.setFont(font)
		self.button_transportation_kollin_add.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_transportation_kollin_add.setObjectName("button_transportation_kollin_add")
		self.button_transportation_kollin_return = QtWidgets.QPushButton(self.tab_transportation)
		self.button_transportation_kollin_return.setGeometry(QtCore.QRect(640, 300, 101, 51))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_transportation_kollin_return.setFont(font)
		self.button_transportation_kollin_return.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_transportation_kollin_return.setObjectName("button_transportation_kollin_return")
		self.label_17 = QtWidgets.QLabel(self.tab_transportation)
		self.label_17.setGeometry(QtCore.QRect(560, 250, 61, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.label_17.setFont(font)
		self.label_17.setObjectName("label_17")
		self.line_12 = QtWidgets.QFrame(self.tab_transportation)
		self.line_12.setGeometry(QtCore.QRect(530, 270, 118, 3))
		self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_12.setObjectName("line_12")
		self.line_13 = QtWidgets.QFrame(self.tab_transportation)
		self.line_13.setGeometry(QtCore.QRect(120, 280, 118, 3))
		self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_13.setObjectName("line_13")
		self.button_transportation_update = QtWidgets.QPushButton(self.tab_transportation)
		self.button_transportation_update.setGeometry(QtCore.QRect(660, 0, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_transportation_update.setFont(font)
		self.button_transportation_update.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_transportation_update.setObjectName("button_transportation_update")
		self.tabWidget.addTab(self.tab_transportation, "")
		self.tab_furniture = QtWidgets.QWidget()
		self.tab_furniture.setObjectName("tab_furniture")
		self.label = QtWidgets.QLabel(self.tab_furniture)
		self.label.setGeometry(QtCore.QRect(280, 10, 221, 51))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.lineEdit_furniture_company = QtWidgets.QLineEdit(self.tab_furniture)
		self.lineEdit_furniture_company.setGeometry(QtCore.QRect(90, 70, 321, 31))
		self.lineEdit_furniture_company.setCompleter(completer_companies_registerd)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.lineEdit_furniture_company.setFont(font)
		self.lineEdit_furniture_company.setText("")
		self.lineEdit_furniture_company.setClearButtonEnabled(False)
		self.lineEdit_furniture_company.setObjectName("lineEdit_furniture_company")
		self.button_furniture_search = QtWidgets.QPushButton(self.tab_furniture)
		self.button_furniture_search.setGeometry(QtCore.QRect(450, 70, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_furniture_search.setFont(font)
		self.button_furniture_search.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_furniture_search.setObjectName("button_furniture_search")
		self.line = QtWidgets.QFrame(self.tab_furniture)
		self.line.setGeometry(QtCore.QRect(0, 110, 771, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.line_2 = QtWidgets.QFrame(self.tab_furniture)
		self.line_2.setGeometry(QtCore.QRect(370, 120, 41, 411))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_3 = QtWidgets.QLabel(self.tab_furniture)
		self.label_3.setGeometry(QtCore.QRect(10, 140, 81, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.tab_furniture)
		self.label_4.setGeometry(QtCore.QRect(410, 140, 121, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.tab_furniture)
		self.label_5.setGeometry(QtCore.QRect(620, 430, 151, 161))
		self.label_5.setText("")
		self.label_5.setPixmap(QtGui.QPixmap("../images/logga-fyrkant.png"))
		self.label_5.setScaledContents(True)
		self.label_5.setObjectName("label_5")
		self.comboBox_furniture_extra = QtWidgets.QComboBox(self.tab_furniture)
		self.comboBox_furniture_extra.setGeometry(QtCore.QRect(580, 140, 171, 31))
		self.comboBox_furniture_extra.addItems(util.all_extra_funiture())
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.comboBox_furniture_extra.setFont(font)
		self.comboBox_furniture_extra.setObjectName("comboBox_furniture_extra")
		self.button_furniture_extra_add = QtWidgets.QPushButton(self.tab_furniture)
		self.button_furniture_extra_add.setGeometry(QtCore.QRect(460, 200, 101, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_furniture_extra_add.setFont(font)
		self.button_furniture_extra_add.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_furniture_extra_add.setObjectName("button_furniture_extra_add")
		self.button_furniture_extra_return = QtWidgets.QPushButton(self.tab_furniture)
		self.button_furniture_extra_return.setGeometry(QtCore.QRect(610, 200, 101, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_furniture_extra_return.setFont(font)
		self.button_furniture_extra_return.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_furniture_extra_return.setObjectName("button_furniture_extra_return")
		self.textBrowser_furniture_extra = QtWidgets.QTextBrowser(self.tab_furniture)
		self.textBrowser_furniture_extra.setGeometry(QtCore.QRect(410, 270, 361, 211))
		self.textBrowser_furniture_extra.setObjectName("textBrowser_furniture_extra")
		self.comboBox_furniture_furniture = QtWidgets.QComboBox(self.tab_furniture)
		self.comboBox_furniture_furniture.setGeometry(QtCore.QRect(100, 140, 261, 31))
		self.comboBox_furniture_furniture.addItems(util.all_furniture())
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.comboBox_furniture_furniture.setFont(font)
		self.comboBox_furniture_furniture.setObjectName("comboBox_furniture_furniture")
		self.textBrowser_furniture_furniture = QtWidgets.QTextBrowser(self.tab_furniture)
		self.textBrowser_furniture_furniture.setGeometry(QtCore.QRect(10, 270, 361, 211))
		self.textBrowser_furniture_furniture.setObjectName("textBrowser_furniture_furniture")
		self.button_furniture_return = QtWidgets.QPushButton(self.tab_furniture)
		self.button_furniture_return.setGeometry(QtCore.QRect(210, 200, 101, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_furniture_return.setFont(font)
		self.button_furniture_return.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_furniture_return.setObjectName("button_furniture_return")
		self.button_furniture_get = QtWidgets.QPushButton(self.tab_furniture)
		self.button_furniture_get.setGeometry(QtCore.QRect(60, 200, 101, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_furniture_get.setFont(font)
		self.button_furniture_get.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_furniture_get.setObjectName("button_furniture_get")
		self.button_furniture_update = QtWidgets.QPushButton(self.tab_furniture)
		self.button_furniture_update.setGeometry(QtCore.QRect(650, 0, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_furniture_update.setFont(font)
		self.button_furniture_update.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_furniture_update.setObjectName("button_furniture_update")
		self.tabWidget.addTab(self.tab_furniture, "")
		self.tab_lack = QtWidgets.QWidget()
		self.tab_lack.setObjectName("tab_lack")
		self.line_7 = QtWidgets.QFrame(self.tab_lack)
		self.line_7.setGeometry(QtCore.QRect(0, 110, 771, 16))
		self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.lineEdit_lack_company = QtWidgets.QLineEdit(self.tab_lack)
		self.lineEdit_lack_company.setGeometry(QtCore.QRect(120, 40, 321, 31))
		self.lineEdit_lack_company.setCompleter(completer_companies_registerd)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.lineEdit_lack_company.setFont(font)
		self.lineEdit_lack_company.setText("")
		self.lineEdit_lack_company.setClearButtonEnabled(False)
		self.lineEdit_lack_company.setObjectName("lineEdit_lack_company")
		self.lineEdit_lack_problem = QtWidgets.QLineEdit(self.tab_lack)
		self.lineEdit_lack_problem.setGeometry(QtCore.QRect(120, 80, 171, 21))
		self.lineEdit_lack_problem.setObjectName("lineEdit_lack_problem")
		self.button_lack_register = QtWidgets.QPushButton(self.tab_lack)
		self.button_lack_register.setGeometry(QtCore.QRect(460, 40, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_lack_register.setFont(font)
		self.button_lack_register.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_lack_register.setObjectName("button_lack_register")
		self.label_11 = QtWidgets.QLabel(self.tab_lack)
		self.label_11.setGeometry(QtCore.QRect(300, 0, 121, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.label_11.setFont(font)
		self.label_11.setObjectName("label_11")
		self.comboBox_lack_furniture = QtWidgets.QComboBox(self.tab_lack)
		self.comboBox_lack_furniture.setGeometry(QtCore.QRect(308, 80, 191, 16))
		self.comboBox_lack_furniture.addItems(util.all_furniture())
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(8)
		self.comboBox_lack_furniture.setFont(font)
		self.comboBox_lack_furniture.setObjectName("comboBox_lack_furniture")
		self.label_12 = QtWidgets.QLabel(self.tab_lack)
		self.label_12.setGeometry(QtCore.QRect(620, 430, 151, 161))
		self.label_12.setText("")
		self.label_12.setPixmap(QtGui.QPixmap("../images/logga-fyrkant.png"))
		self.label_12.setScaledContents(True)
		self.label_12.setObjectName("label_12")
		self.button_lack_update = QtWidgets.QPushButton(self.tab_lack)
		self.button_lack_update.setGeometry(QtCore.QRect(650, 130, 111, 32))
		font = QtGui.QFont()
		font.setFamily("Arial")
		#font.setPointSize(-1)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.button_lack_update.setFont(font)
		self.button_lack_update.setStyleSheet("QPushButton{\n"
	"background-color:#a6192e;\n"
	"color: white;\n"
	"border-style: outset;\n"
	"border-width: 2px;\n"
	"border-radius: 10px;\n"
	"border-color: beige;\n"
	"font: bold 14px;\n"
	"min-width: 5em;\n"
	"padding: 6px;\n"
	"}\n"
	"QPushButton:hover {\n"
	"background-color: #f52e4c;\n"
	"}\n"
	"QPushButton:pressed {\n"
	"background-color: #36ff00;\n"
	"}")
		self.button_lack_update.setObjectName("button_lack_update")
		self.comboBox_lack_company = QtWidgets.QComboBox(self.tab_lack)
		self.comboBox_lack_company.setGeometry(QtCore.QRect(490, 180, 271, 31))
		self.comboBox_lack_company.addItems(util.all_furniture())
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.comboBox_lack_company.setFont(font)
		self.comboBox_lack_company.setObjectName("comboBox_lack_company")
		self.label_13 = QtWidgets.QLabel(self.tab_lack)
		self.label_13.setGeometry(QtCore.QRect(30, 130, 141, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(15)
		self.label_13.setFont(font)
		self.label_13.setObjectName("label_13")
		self.textBrowser_lack = QtWidgets.QTextBrowser(self.tab_lack)
		self.textBrowser_lack.setGeometry(QtCore.QRect(30, 180, 441, 311))
		self.textBrowser_lack.setObjectName("textBrowser_lack")
		self.tabWidget.addTab(self.tab_lack, "")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(3)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# When buttons are clickd, it is triggered here
		## Storage 
		self.button_storage_search.clicked.connect(lambda: buttons.storage_search(self))
		self.button_storage_update.clicked.connect(lambda: buttons.storage_update(self))
		self.button_storage_checkin.clicked.connect(lambda: buttons.storage_checkin(self, self.db))
		self.button_storage_checkout.clicked.connect(lambda: buttons.storage_checkout(self, self.db))
		self.button_storage_borrow.clicked.connect(lambda: buttons.storage_borrow(self, self.db))
		self.button_storage_return.clicked.connect(lambda: buttons.storage_return(self, self.db))

		## Transportation
		self.button_transportation_search.clicked.connect(lambda: buttons.transportation_search(self))
		self.button_transportation_update.clicked.connect(lambda: buttons.transportation_update(self))
		self.button_transportation_register.clicked.connect(lambda: buttons.transportation_register(self, self.db))
		self.button_transportation_send.clicked.connect(lambda: buttons.transportation_send(self, self.db))
		self.button_transportation_kollin_add.clicked.connect(lambda: buttons.transportation_kollin_add(self))
		self.button_transportation_kollin_return.clicked.connect(lambda: buttons.transportation_kollin_return(self))
		
		## Furniture page
		self.button_furniture_search.clicked.connect(lambda: buttons.furniture_search(self))
		self.button_furniture_update.clicked.connect(lambda: buttons.furniture_update(self))
		self.button_furniture_get.clicked.connect(lambda: buttons.furniture_get(self, self.db))
		self.button_furniture_return.clicked.connect(lambda: buttons.furniture_return(self, self.db))
		self.button_furniture_extra_add.clicked.connect(lambda: buttons.furniture_extra_add(self))
		self.button_furniture_extra_return.clicked.connect(lambda: buttons.furniture_extra_return(self))

		## lack page
		self.button_lack_register.clicked.connect(lambda: buttons.lack_register(self))
		self.button_lack_update.clicked.connect(lambda: buttons.lack_update(self))

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Företagsmöbler - LARV"))
		self.button_storage_search.setText(_translate("MainWindow", "Sök"))
		self.button_storage_search.setShortcut(_translate("MainWindow", "Return"))
		self.label_6.setText(_translate("MainWindow", "Lager för företag"))
		self.label_7.setText(_translate("MainWindow", "Palldragare - Låna"))
		self.lineEdit_storage_name.setPlaceholderText(_translate("MainWindow", "Företag"))
		self.lineEdit_storage_borrow_id.setPlaceholderText(_translate("MainWindow", "Palldragare"))
		self.button_storage_borrow.setText(_translate("MainWindow", "Låna"))
		self.button_storage_borrow.setShortcut(_translate("MainWindow", "Return"))
		self.label_8.setText(_translate("MainWindow", "Palldragare - Lämna"))
		self.lineEdit_storage_return_id.setPlaceholderText(_translate("MainWindow", "Palldragare"))
		self.button_storage_return.setText(_translate("MainWindow", "Lämna"))
		self.button_storage_return.setShortcut(_translate("MainWindow", "Return"))
		self.button_storage_checkin.setText(_translate("MainWindow", "Checka in"))
		self.button_storage_checkin.setShortcut(_translate("MainWindow", "Return"))
		self.button_storage_checkout.setText(_translate("MainWindow", "Checka ut"))
		self.button_storage_checkout.setShortcut(_translate("MainWindow", "Return"))
		self.gui_func.updateStatus(window=self.textBrowser_storage) # This is just setting up the window for "storage"
		self.button_storage_update.setText(_translate("MainWindow", "Uppdatera"))
		self.button_storage_update.setShortcut(_translate("MainWindow", "Return"))
		self.lineEdit_storage_company.setPlaceholderText(_translate("MainWindow", "Företagsnamnet"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_storage), _translate("MainWindow", "Lager"))
		self.label_10.setText(_translate("MainWindow", "Transport"))
		self.lineEdit_transportation_company.setPlaceholderText(_translate("MainWindow", "Företagsnamnet"))
		self.gui_func.updateStatus(window=self.textBrowser_transportation) # This is just setting up the window for "transportation"
		self.button_transportation_search.setText(_translate("MainWindow", "Sök"))
		self.button_transportation_search.setShortcut(_translate("MainWindow", "Return"))
		self.label_16.setText(_translate("MainWindow", "Registrera lagerplats"))
		self.button_transportation_register.setText(_translate("MainWindow", "Registrera"))
		self.button_transportation_register.setShortcut(_translate("MainWindow", "Return"))
		self.lineEdit_transportation_id.setPlaceholderText(_translate("MainWindow", "Lagerplats"))
		self.button_transportation_send.setText(_translate("MainWindow", "Bekräfta och skicka"))
		self.button_transportation_send.setShortcut(_translate("MainWindow", "Return"))
		self.button_transportation_kollin_add.setText(_translate("MainWindow", "+1"))
		self.button_transportation_kollin_add.setShortcut(_translate("MainWindow", "Return"))
		self.button_transportation_kollin_return.setText(_translate("MainWindow", "-1"))
		self.button_transportation_kollin_return.setShortcut(_translate("MainWindow", "Return"))
		self.label_17.setText(_translate("MainWindow", "Kollin"))
		self.button_transportation_update.setText(_translate("MainWindow", "Uppdatera"))
		self.button_transportation_update.setShortcut(_translate("MainWindow", "Return"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_transportation), _translate("MainWindow", "Transport"))
		self.label.setText(_translate("MainWindow", "Möbler för företag"))
		self.lineEdit_furniture_company.setPlaceholderText(_translate("MainWindow", "Företagsnamnet"))
		self.button_furniture_search.setText(_translate("MainWindow", "Sök"))
		self.button_furniture_search.setShortcut(_translate("MainWindow", "Return"))
		self.label_3.setText(_translate("MainWindow", "Möbler"))
		self.label_4.setText(_translate("MainWindow", "Extra möbler"))
		self.button_furniture_extra_add.setText(_translate("MainWindow", "+1"))
		self.button_furniture_extra_add.setShortcut(_translate("MainWindow", "Return"))
		self.button_furniture_extra_return.setText(_translate("MainWindow", "-1"))
		self.button_furniture_extra_return.setShortcut(_translate("MainWindow", "Return"))
		self.button_furniture_return.setText(_translate("MainWindow", "Lämna"))
		self.button_furniture_return.setShortcut(_translate("MainWindow", "Return"))
		self.button_furniture_get.setText(_translate("MainWindow", "Hämta"))
		self.button_furniture_get.setShortcut(_translate("MainWindow", "Return"))
		self.button_furniture_update.setText(_translate("MainWindow", "Uppdatera"))
		self.button_furniture_update.setShortcut(_translate("MainWindow", "Return"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_furniture), _translate("MainWindow", "Möbler"))
		self.lineEdit_lack_company.setPlaceholderText(_translate("MainWindow", "Företagsnamnet"))
		self.lineEdit_lack_problem.setPlaceholderText(_translate("MainWindow", "Problem"))
		self.button_lack_register.setText(_translate("MainWindow", "Registrera"))
		self.button_lack_register.setShortcut(_translate("MainWindow", "Return"))
		self.label_11.setText(_translate("MainWindow", "Lägg till fel"))
		self.button_lack_update.setText(_translate("MainWindow", "Uppdatera"))
		self.button_lack_update.setShortcut(_translate("MainWindow", "Return"))
		self.label_13.setText(_translate("MainWindow", "Felanmälningar"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_lack), _translate("MainWindow", "Felanmälning"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
