# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openWindowsui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from functools import partial
import gettext
lng = "es"

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
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(705, 0))
        self.pushButton_2.setObjectName(_fromUtf8("singleSemesterBtn"))
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.lngImG = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lngImG.sizePolicy().hasHeightForWidth())
        self.lngImG.setSizePolicy(sizePolicy)
        self.lngImG.setMinimumSize(QtCore.QSize(0, 0))
        self.lngImG.setText(_fromUtf8(""))
        self.lngImG.setPixmap(QtGui.QPixmap(_fromUtf8("images/neocreoMap.png")))
        self.lngImG.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lngImG.setWordWrap(False)
        self.lngImG.setObjectName(_fromUtf8("lngImG"))
        self.gridLayout_2.addWidget(self.lngImG, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(705, 0))
        self.pushButton.setObjectName(_fromUtf8("fullSemesterBtn"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(partial(self.printBtn,self.pushButton_2.objectName(),Form))
        self.pushButton.clicked.connect(partial(self.printBtn,self.pushButton.objectName(),Form))
        self.lngImG.mousePressEvent = partial(self.print_some)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", _('Single Semester'), None))
        self.pushButton.setText(_translate("Form", _('Complete Year'), None))

    def printBtn(self,btn,Form):
        print(btn)

    def print_some(self,event):
        print("Clicked, from")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
