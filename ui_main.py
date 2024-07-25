# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 707)
        MainWindow.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{border:none;}\n"
"\n"
"QLabel{color: rgb(255, 255, 255);}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, -1)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(0, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.left_container)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, 0, 0)
        self.top_frame = QFrame(self.left_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.top_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_logo_2 = QLabel(self.top_frame)
        self.label_logo_2.setObjectName(u"label_logo_2")
        self.label_logo_2.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Sitka Text Semibold"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_logo_2.setFont(font)
        self.label_logo_2.setStyleSheet(u"")
        self.label_logo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_logo_2)


        self.gridLayout_4.addWidget(self.top_frame, 0, 0, 1, 1)

        self.botton_frame = QFrame(self.left_container)
        self.botton_frame.setObjectName(u"botton_frame")
        self.botton_frame.setStyleSheet(u"QFrame{background-color: rgb(65, 65, 65);}\n"
"\n"
"QToolBox{background-color: rgb(288, 254, 255);}\n"
"\n"
"QToolBox::tab{border-radius: 5px; background-color: rgb(162, 102, 233)}")
        self.botton_frame.setFrameShape(QFrame.StyledPanel)
        self.botton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.botton_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.botton_frame)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"border-top-left-radius: 10px")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setGeometry(QRect(0, 0, 107, 532))
        self.verticalLayout_8 = QVBoxLayout(self.page_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_menu_home = QPushButton(self.page_1)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        self.btn_menu_home.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_menu_home.setFont(font1)
        self.btn_menu_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_home.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(65, 65, 65);\n"
"border-top-left-radius: 10px\n"
"}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);}")

        self.verticalLayout_8.addWidget(self.btn_menu_home)

        self.btn_menu_receitas = QPushButton(self.page_1)
        self.btn_menu_receitas.setObjectName(u"btn_menu_receitas")
        self.btn_menu_receitas.setMinimumSize(QSize(0, 30))
        self.btn_menu_receitas.setFont(font1)
        self.btn_menu_receitas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_receitas.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(65, 65, 65);\n"
"border-top-left-radius: 10px\n"
"}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);}")

        self.verticalLayout_8.addWidget(self.btn_menu_receitas)

        self.btn_menu_criar = QPushButton(self.page_1)
        self.btn_menu_criar.setObjectName(u"btn_menu_criar")
        self.btn_menu_criar.setMinimumSize(QSize(0, 30))
        self.btn_menu_criar.setFont(font1)
        self.btn_menu_criar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_criar.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(65, 65, 65);\n"
"border-top-left-radius: 10px\n"
"}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);}")

        self.verticalLayout_8.addWidget(self.btn_menu_criar)

        self.btn_menu_cadastrar = QPushButton(self.page_1)
        self.btn_menu_cadastrar.setObjectName(u"btn_menu_cadastrar")
        self.btn_menu_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_menu_cadastrar.setFont(font1)
        self.btn_menu_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_cadastrar.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(65, 65, 65);\n"
"border-top-left-radius: 10px\n"
"}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);}")

        self.verticalLayout_8.addWidget(self.btn_menu_cadastrar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page_1, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 170, 532))
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        self.label_2.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_2)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.gridLayout_4.addWidget(self.botton_frame, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.left_container)

        self.right_container = QFrame(self.centralwidget)
        self.right_container.setObjectName(u"right_container")
        self.right_container.setFrameShape(QFrame.StyledPanel)
        self.right_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_1 = QFrame(self.right_container)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMaximumSize(QSize(16777215, 50))
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_toggle_home = QPushButton(self.frame_1)
        self.btn_toggle_home.setObjectName(u"btn_toggle_home")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_home.sizePolicy().hasHeightForWidth())
        self.btn_toggle_home.setSizePolicy(sizePolicy)
        self.btn_toggle_home.setMinimumSize(QSize(75, 0))
        self.btn_toggle_home.setSizeIncrement(QSize(0, 0))
        self.btn_toggle_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu_rox.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle_home.setIcon(icon)
        self.btn_toggle_home.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.btn_toggle_home, 0, 0, 1, 1)

        self.label_top = QLabel(self.frame_1)
        self.label_top.setObjectName(u"label_top")
        self.label_top.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Sitka Text Semibold"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_top.setFont(font3)
        self.label_top.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_top, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_1)

        self.main_frame = QFrame(self.right_container)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout_2 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Sitka Text Semibold"])
        font4.setPointSize(72)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.pages.addWidget(self.pg_home)
        self.pg_receitas = QWidget()
        self.pg_receitas.setObjectName(u"pg_receitas")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_receitas)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.frame_3 = QFrame(self.pg_receitas)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(213, 213, 213);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_receitas = QLabel(self.frame_3)
        self.label_receitas.setObjectName(u"label_receitas")

        self.verticalLayout_5.addWidget(self.label_receitas)

        self.tableWidget_receitas = QTableWidget(self.frame_3)
        if (self.tableWidget_receitas.columnCount() < 1):
            self.tableWidget_receitas.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_receitas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_receitas.setObjectName(u"tableWidget_receitas")
        self.tableWidget_receitas.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"gridline-color: rgb(0, 0, 0);\n"
"color:#000000")

        self.verticalLayout_5.addWidget(self.tableWidget_receitas)

        self.btn_receitas_abrir = QPushButton(self.frame_3)
        self.btn_receitas_abrir.setObjectName(u"btn_receitas_abrir")
        self.btn_receitas_abrir.setMinimumSize(QSize(0, 25))
        self.btn_receitas_abrir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-radius:15px;\n"
"	color:#ffffff\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:  rgb(162, 102, 233);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_receitas_abrir)

        self.btn_receitas_excluir = QPushButton(self.frame_3)
        self.btn_receitas_excluir.setObjectName(u"btn_receitas_excluir")
        self.btn_receitas_excluir.setMinimumSize(QSize(0, 25))
        self.btn_receitas_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-radius:15px;\n"
"	color:#ffffff\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:  rgb(162, 102, 233);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_receitas_excluir)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pages.addWidget(self.pg_receitas)
        self.pg_criar = QWidget()
        self.pg_criar.setObjectName(u"pg_criar")
        self.gridLayout = QGridLayout(self.pg_criar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_nome = QLineEdit(self.pg_criar)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_nome.sizePolicy().hasHeightForWidth())
        self.lineEdit_nome.setSizePolicy(sizePolicy1)
        self.lineEdit_nome.setMinimumSize(QSize(0, 20))
        self.lineEdit_nome.setMaximumSize(QSize(16777215, 16777213))
        self.lineEdit_nome.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"color: #000000")

        self.gridLayout.addWidget(self.lineEdit_nome, 0, 0, 1, 2)

        self.lineEdit_lucro = QLineEdit(self.pg_criar)
        self.lineEdit_lucro.setObjectName(u"lineEdit_lucro")
        self.lineEdit_lucro.setMinimumSize(QSize(0, 20))
        self.lineEdit_lucro.setMaximumSize(QSize(250, 16777215))
        font5 = QFont()
        font5.setPointSize(10)
        self.lineEdit_lucro.setFont(font5)
        self.lineEdit_lucro.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"color: #000000")
        self.lineEdit_lucro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_lucro, 0, 2, 1, 1)

        self.lineEdit_qtd = QLineEdit(self.pg_criar)
        self.lineEdit_qtd.setObjectName(u"lineEdit_qtd")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_qtd.sizePolicy().hasHeightForWidth())
        self.lineEdit_qtd.setSizePolicy(sizePolicy2)
        self.lineEdit_qtd.setMinimumSize(QSize(0, 20))
        self.lineEdit_qtd.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_qtd.setSizeIncrement(QSize(0, 0))
        self.lineEdit_qtd.setBaseSize(QSize(0, 0))
        self.lineEdit_qtd.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"color: #000000")

        self.gridLayout.addWidget(self.lineEdit_qtd, 0, 3, 1, 1)

        self.tableWidget_criar = QTableWidget(self.pg_criar)
        if (self.tableWidget_criar.columnCount() < 4):
            self.tableWidget_criar.setColumnCount(4)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_criar.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_criar.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_criar.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_criar.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        if (self.tableWidget_criar.rowCount() < 29):
            self.tableWidget_criar.setRowCount(29)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(12, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(13, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(14, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(15, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(16, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(17, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(18, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(19, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(20, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(21, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(22, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(23, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(24, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(25, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(26, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(27, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_criar.setVerticalHeaderItem(28, __qtablewidgetitem33)
        self.tableWidget_criar.setObjectName(u"tableWidget_criar")
        self.tableWidget_criar.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"color: #000000")

        self.gridLayout.addWidget(self.tableWidget_criar, 1, 0, 1, 4)

        self.label_valor_total = QLabel(self.pg_criar)
        self.label_valor_total.setObjectName(u"label_valor_total")
        self.label_valor_total.setMinimumSize(QSize(0, 20))
        self.label_valor_total.setMaximumSize(QSize(300, 20))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_valor_total.setFont(font6)

        self.gridLayout.addWidget(self.label_valor_total, 2, 0, 1, 1)

        self.label_vt = QLabel(self.pg_criar)
        self.label_vt.setObjectName(u"label_vt")

        self.gridLayout.addWidget(self.label_vt, 2, 1, 1, 1)

        self.btn_salvar_receita = QPushButton(self.pg_criar)
        self.btn_salvar_receita.setObjectName(u"btn_salvar_receita")
        self.btn_salvar_receita.setMinimumSize(QSize(0, 20))
        self.btn_salvar_receita.setMaximumSize(QSize(200, 16777215))
        self.btn_salvar_receita.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-radius:5px;\n"
"	color:#ffffff\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color:  rgb(162, 102, 233);\n"
"}")

        self.gridLayout.addWidget(self.btn_salvar_receita, 2, 3, 1, 1)

        self.label_valor_total_lucro = QLabel(self.pg_criar)
        self.label_valor_total_lucro.setObjectName(u"label_valor_total_lucro")
        self.label_valor_total_lucro.setMinimumSize(QSize(0, 20))
        self.label_valor_total_lucro.setMaximumSize(QSize(300, 20))
        self.label_valor_total_lucro.setFont(font6)

        self.gridLayout.addWidget(self.label_valor_total_lucro, 3, 0, 1, 1)

        self.label_vtl = QLabel(self.pg_criar)
        self.label_vtl.setObjectName(u"label_vtl")

        self.gridLayout.addWidget(self.label_vtl, 3, 1, 1, 1)

        self.btn_calcular = QPushButton(self.pg_criar)
        self.btn_calcular.setObjectName(u"btn_calcular")
        self.btn_calcular.setMinimumSize(QSize(0, 20))
        self.btn_calcular.setMaximumSize(QSize(200, 16777215))
        self.btn_calcular.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-radius:5px;\n"
"	color:#ffffff\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color:  rgb(162, 102, 233);\n"
"}")

        self.gridLayout.addWidget(self.btn_calcular, 3, 3, 1, 1)

        self.label_valor_unitario = QLabel(self.pg_criar)
        self.label_valor_unitario.setObjectName(u"label_valor_unitario")
        self.label_valor_unitario.setMinimumSize(QSize(0, 0))
        self.label_valor_unitario.setMaximumSize(QSize(300, 20))
        self.label_valor_unitario.setFont(font6)

        self.gridLayout.addWidget(self.label_valor_unitario, 4, 0, 1, 1)

        self.label_vu = QLabel(self.pg_criar)
        self.label_vu.setObjectName(u"label_vu")

        self.gridLayout.addWidget(self.label_vu, 4, 1, 1, 1)

        self.pages.addWidget(self.pg_criar)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_10 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"color:#000000;\n"
"QTabBar::tab:selected {\n"
"    background: #ffffff;\n"
"    color: #000;\n"
"}")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.tab_1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame = QFrame(self.tab_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_produto = QLineEdit(self.frame)
        self.lineEdit_produto.setObjectName(u"lineEdit_produto")
        self.lineEdit_produto.setMinimumSize(QSize(600, 20))
        self.lineEdit_produto.setStyleSheet(u"background-color: rgb(205, 205, 205);\n"
"color: #000000;\n"
"border-radius: 5px;")
        self.lineEdit_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_produto, 1, 1, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(600, 31))
        self.btn_cadastrar.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setPointSize(13)
        self.btn_cadastrar.setFont(font7)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-radius:15px;\n"
"	color:#ffffff\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:  rgb(162, 102, 233);\n"
"}")

        self.gridLayout_3.addWidget(self.btn_cadastrar, 5, 1, 1, 2)

        self.lineEdit_unidade = QLineEdit(self.frame)
        self.lineEdit_unidade.setObjectName(u"lineEdit_unidade")
        self.lineEdit_unidade.setMinimumSize(QSize(600, 20))
        self.lineEdit_unidade.setStyleSheet(u"background-color: rgb(205, 205, 205);\n"
"color: #000000;\n"
"border-radius: 5px;")
        self.lineEdit_unidade.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_unidade, 2, 1, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEdit_quantidade = QLineEdit(self.frame)
        self.lineEdit_quantidade.setObjectName(u"lineEdit_quantidade")
        self.lineEdit_quantidade.setMinimumSize(QSize(600, 20))
        self.lineEdit_quantidade.setStyleSheet(u"background-color: rgb(205, 205, 205);\n"
"color: #000000;\n"
"border-radius: 5px;")
        self.lineEdit_quantidade.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_quantidade, 3, 1, 1, 2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)

        self.lineEdit_valor = QLineEdit(self.frame)
        self.lineEdit_valor.setObjectName(u"lineEdit_valor")
        self.lineEdit_valor.setMinimumSize(QSize(600, 20))
        self.lineEdit_valor.setStyleSheet(u"background-color: rgb(205, 205, 205);\n"
"color: #000000;\n"
"border-radius: 5px;")
        self.lineEdit_valor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_valor, 4, 1, 1, 2)

        self.error_label = QLabel(self.frame)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setMaximumSize(QSize(16777215, 30))
        self.error_label.setFont(font5)

        self.gridLayout_3.addWidget(self.error_label, 6, 1, 1, 2, Qt.AlignHCenter)

        self.label_cadastro = QLabel(self.frame)
        self.label_cadastro.setObjectName(u"label_cadastro")

        self.gridLayout_3.addWidget(self.label_cadastro, 0, 0, 1, 3, Qt.AlignTop)

        self.verticalSpacer_4 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 7, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"color: #000000")
        self.verticalLayout_13 = QVBoxLayout(self.tab_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_1_tab2 = QFrame(self.tab_2)
        self.frame_1_tab2.setObjectName(u"frame_1_tab2")
        self.frame_1_tab2.setFrameShape(QFrame.StyledPanel)
        self.frame_1_tab2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_1_tab2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_frame_1 = QLabel(self.frame_1_tab2)
        self.label_frame_1.setObjectName(u"label_frame_1")
        self.label_frame_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_frame_1)


        self.verticalLayout_13.addWidget(self.frame_1_tab2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget_produtos = QTableWidget(self.tab_2)
        if (self.tableWidget_produtos.columnCount() < 4):
            self.tableWidget_produtos.setColumnCount(4)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_produtos.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_produtos.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_produtos.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_produtos.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        self.tableWidget_produtos.setObjectName(u"tableWidget_produtos")
        self.tableWidget_produtos.setStyleSheet(u"background-color: rgb(245, 245, 245);")

        self.horizontalLayout_3.addWidget(self.tableWidget_produtos)

        self.frame_2_tab2 = QFrame(self.tab_2)
        self.frame_2_tab2.setObjectName(u"frame_2_tab2")
        self.frame_2_tab2.setFrameShape(QFrame.StyledPanel)
        self.frame_2_tab2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2_tab2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.btn_alterar = QPushButton(self.frame_2_tab2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(60, 20))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-radius:15px;\n"
"	color:#ffffff\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:  rgb(162, 102, 233);\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_2_tab2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(60, 20))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-radius:15px;\n"
"	color:#ffffff\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:  rgb(162, 102, 233);\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_2_tab2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_10.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_cadastrar)

        self.verticalLayout_6.addWidget(self.pages)


        self.verticalLayout_4.addWidget(self.main_frame)

        self.frame_2 = QFrame(self.right_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_dev = QLabel(self.frame_2)
        self.label_dev.setObjectName(u"label_dev")
        font8 = QFont()
        font8.setFamilies([u"Calibri"])
        font8.setPointSize(10)
        font8.setBold(False)
        self.label_dev.setFont(font8)
        self.label_dev.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_dev)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.right_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_logo_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#a266e9;\">Az</span></p></body></html>", None))
        self.btn_menu_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_menu_receitas.setText(QCoreApplication.translate("MainWindow", u"Receitas", None))
        self.btn_menu_criar.setText(QCoreApplication.translate("MainWindow", u"Criar Receita", None))
        self.btn_menu_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">Desenvolvido por: </span><span style=\" font-size:7pt;\">Rafael Botelho</span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">Contato:</span><span style=\" font-size:7pt;\"> (11) 94072-4816</span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">Email:</span><span style=\" font-size:7pt;\"> rafaelbotelho@live.com</span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">Sistema:</span><span style=\" font-size:7pt;\"> Cadastro e C\u00e1lculo</span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">Status:</span><span style=\" font-size:7pt;\"> Ativo</span></p><p align=\"center\"><span style=\" font-size:7pt;\"><br/></span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toggle_home.setText("")
        self.label_top.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sistema para calcular o custo de produ\u00e7\u00e3o</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:72pt; color:#a366e9;\">Az</span></p></body></html>", None))
        self.label_receitas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">SUAS RECEITAS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_receitas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"RECEITAS", None));
        self.btn_receitas_abrir.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.btn_receitas_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.lineEdit_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DA RECEITA", None))
        self.lineEdit_lucro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DEFINA O LUCRO DESEJADO", None))
        self.lineEdit_qtd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QUANTIDADE PRODUZIDA", None))
        ___qtablewidgetitem1 = self.tableWidget_criar.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));
        ___qtablewidgetitem2 = self.tableWidget_criar.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"UNIDADE", None));
        ___qtablewidgetitem3 = self.tableWidget_criar.horizontalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem4 = self.tableWidget_criar.horizontalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        ___qtablewidgetitem5 = self.tableWidget_criar.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"01", None));
        ___qtablewidgetitem6 = self.tableWidget_criar.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"02", None));
        ___qtablewidgetitem7 = self.tableWidget_criar.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"03", None));
        ___qtablewidgetitem8 = self.tableWidget_criar.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"04", None));
        ___qtablewidgetitem9 = self.tableWidget_criar.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"05", None));
        ___qtablewidgetitem10 = self.tableWidget_criar.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"06", None));
        ___qtablewidgetitem11 = self.tableWidget_criar.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"07", None));
        ___qtablewidgetitem12 = self.tableWidget_criar.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"08", None));
        ___qtablewidgetitem13 = self.tableWidget_criar.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"09", None));
        ___qtablewidgetitem14 = self.tableWidget_criar.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem15 = self.tableWidget_criar.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem16 = self.tableWidget_criar.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem17 = self.tableWidget_criar.verticalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem18 = self.tableWidget_criar.verticalHeaderItem(13)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem19 = self.tableWidget_criar.verticalHeaderItem(14)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem20 = self.tableWidget_criar.verticalHeaderItem(15)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem21 = self.tableWidget_criar.verticalHeaderItem(16)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem22 = self.tableWidget_criar.verticalHeaderItem(17)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem23 = self.tableWidget_criar.verticalHeaderItem(18)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem24 = self.tableWidget_criar.verticalHeaderItem(19)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem25 = self.tableWidget_criar.verticalHeaderItem(20)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem26 = self.tableWidget_criar.verticalHeaderItem(21)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem27 = self.tableWidget_criar.verticalHeaderItem(22)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem28 = self.tableWidget_criar.verticalHeaderItem(23)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"24", None));
        ___qtablewidgetitem29 = self.tableWidget_criar.verticalHeaderItem(24)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"25", None));
        ___qtablewidgetitem30 = self.tableWidget_criar.verticalHeaderItem(25)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem31 = self.tableWidget_criar.verticalHeaderItem(26)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"27", None));
        ___qtablewidgetitem32 = self.tableWidget_criar.verticalHeaderItem(27)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"28", None));
        ___qtablewidgetitem33 = self.tableWidget_criar.verticalHeaderItem(28)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"30", None));
        self.label_valor_total.setText(QCoreApplication.translate("MainWindow", u"VALOR TOTAL DA RECEITA :", None))
        self.label_vt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.btn_salvar_receita.setText(QCoreApplication.translate("MainWindow", u"SALVAR RECEITA", None))
        self.label_valor_total_lucro.setText(QCoreApplication.translate("MainWindow", u"VALOR TOTAL + LUCRO SOBRE CUSTO:", None))
        self.label_vtl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.btn_calcular.setText(QCoreApplication.translate("MainWindow", u"CALCULAR VALORES", None))
        self.label_valor_unitario.setText(QCoreApplication.translate("MainWindow", u"VALOR UNIT\u00c1RIO + LUCRO SOBRE CUSTO:", None))
        self.label_vu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PRODUTO:", None))
        self.lineEdit_produto.setText("")
        self.lineEdit_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"UNIDADE:", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.lineEdit_unidade.setText("")
        self.lineEdit_unidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UNIDADE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE:", None))
        self.lineEdit_quantidade.setText("")
        self.lineEdit_quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"VALOR:", None))
        self.lineEdit_valor.setText("")
        self.lineEdit_valor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR", None))
        self.error_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#2f2f2f;\">Cadastre aqui seus Produtos e Servi\u00e7os</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_frame_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#2b2b2b;\">Produtos</span></p></body></html>", None))
        ___qtablewidgetitem34 = self.tableWidget_produtos.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));
        ___qtablewidgetitem35 = self.tableWidget_produtos.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"UNIDADE", None));
        ___qtablewidgetitem36 = self.tableWidget_produtos.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem37 = self.tableWidget_produtos.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.label_dev.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por: Rafael Botelho - Az", None))
    # retranslateUi

