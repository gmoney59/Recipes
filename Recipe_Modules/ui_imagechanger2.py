# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_imagechanger2.ui'
#
# Created: Wed Dec 23 11:39:05 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1317, 845)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.home = QtGui.QWidget()
        self.home.setObjectName(_fromUtf8("home"))
        self.verticalLayout = QtGui.QVBoxLayout(self.home)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.home)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.tabWidget.addTab(self.home, _fromUtf8(""))
        self.dinner = QtGui.QWidget()
        self.dinner.setObjectName(_fromUtf8("dinner"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dinner)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.listView_2 = QtGui.QListView(self.dinner)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.verticalLayout_2.addWidget(self.listView_2)
        self.tabWidget.addTab(self.dinner, _fromUtf8(""))
        self.desserts = QtGui.QWidget()
        self.desserts.setObjectName(_fromUtf8("desserts"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.desserts)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.listView_3 = QtGui.QListView(self.desserts)
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.verticalLayout_4.addWidget(self.listView_3)
        self.tabWidget.addTab(self.desserts, _fromUtf8(""))
        self.misc = QtGui.QWidget()
        self.misc.setObjectName(_fromUtf8("misc"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.misc)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listView_4 = QtGui.QListView(self.misc)
        self.listView_4.setObjectName(_fromUtf8("listView_4"))
        self.verticalLayout_3.addWidget(self.listView_4)
        self.tabWidget.addTab(self.misc, _fromUtf8(""))
        self.extra = QtGui.QWidget()
        self.extra.setObjectName(_fromUtf8("extra"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.extra)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.listWidget = QtGui.QListWidget(self.extra)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_5.addWidget(self.listWidget)
        self.tabWidget.addTab(self.extra, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setFrameShape(QtGui.QFrame.Box)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 991, 784))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.imageLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.horizontalLayout_5.addWidget(self.imageLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pageLabel_2 = QtGui.QTextEdit(self.page_2)
        self.pageLabel_2.setObjectName(_fromUtf8("pageLabel_2"))
        self.horizontalLayout_3.addWidget(self.pageLabel_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.page_3)
        self.videoPlayer.setGeometry(QtCore.QRect(80, 100, 701, 421))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.page_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.scrollArea_2 = QtGui.QScrollArea(self.page_4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 783, 784))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1317, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuMerry_Christmas_Mom = QtGui.QMenu(self.menubar)
        self.menuMerry_Christmas_Mom.setObjectName(_fromUtf8("menuMerry_Christmas_Mom"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_This_Program = QtGui.QAction(MainWindow)
        self.actionAbout_This_Program.setObjectName(_fromUtf8("actionAbout_This_Program"))
        self.menuMerry_Christmas_Mom.addSeparator()
        self.menuMerry_Christmas_Mom.addAction(self.actionAbout_This_Program)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuMerry_Christmas_Mom.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("MainWindow", "Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dinner), _translate("MainWindow", "Dinner", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.desserts), _translate("MainWindow", "Desserts", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.misc), _translate("MainWindow", "Misc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extra), _translate("MainWindow", "Extra", None))
        self.imageLabel.setText(_translate("MainWindow", "", None))
        self.pushButton_1.setText(_translate("MainWindow", "1", None))
        self.pushButton_2.setText(_translate("MainWindow", "2", None))
        self.pushButton_3.setText(_translate("MainWindow", "3", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuMerry_Christmas_Mom.setTitle(_translate("MainWindow", "Merry Christmas Mom!", None))
        self.actionAbout_This_Program.setText(_translate("MainWindow", "About This Program", None))

from PyQt4 import phonon
