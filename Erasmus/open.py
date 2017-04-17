# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openWindowsuiComboBoxLng.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from functools import partial
import gettext
lng = "ch"

langtouse = gettext.translation(lng, localedir='locale', languages=[lng])
langtouse.install()

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1458, 1000)
        Form.setMaximumSize(QtCore.QSize(1458, 1000))
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(705, 0))
        self.pushButton_2.setObjectName(_fromUtf8("singlSem"))
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(218)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(350, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(0, 16777215))
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(705, 0))
        self.pushButton.setObjectName(_fromUtf8("doubleSem"))
        self.gridLayout_2.addWidget(self.pushButton, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", _('Single Semester'), None))
        self.pushButton.setText(_translate("Form", _('Complete Year'), None))
        self.comboBox.addItems(["English","Français","Deutsch","Suomi","Español","中文","Èdè Yorùbá"])


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
