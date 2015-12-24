# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addRecipeDlg.ui'
#
# Created: Wed Dec 23 23:36:07 2015
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

class Ui_addRecipeDialog(object):
    def setupUi(self, addRecipeDialog):
        addRecipeDialog.setObjectName(_fromUtf8("addRecipeDialog"))
        addRecipeDialog.resize(761, 461)
        self.verticalLayout = QtGui.QVBoxLayout(addRecipeDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(addRecipeDialog)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonBox = QtGui.QDialogButtonBox(addRecipeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(addRecipeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), addRecipeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), addRecipeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addRecipeDialog)

    def retranslateUi(self, addRecipeDialog):
        addRecipeDialog.setWindowTitle(_translate("addRecipeDialog", "Dialog", None))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dlg = QtGui.QDialog()
    ui = Ui_addRecipeDialog()
    ui.setupUi(dlg)
    dlg.show()
    app.exec_()

