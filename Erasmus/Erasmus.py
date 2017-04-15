# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Erasmus.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
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

class Ui_Erasmus():


    def loadFile(self):
        countries=[] #Create empty list
        afile=open('countries.txt','r') #Open file for reading
        for line in afile: #iterate through file and add each item to the list
             countries.append(str(line).rstrip('\n'))
        afile.close()

    def setupUi(self, Erasmus):
        Erasmus.setObjectName(_fromUtf8("Erasmus"))
        Erasmus.resize(1297, 820)
        self.horizontalLayout = QtGui.QHBoxLayout(Erasmus)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(Erasmus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 623, 782))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))




        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtGui.QScrollArea(Erasmus)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 588, 938))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        # self.textBrowser_4 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        # self.gridLayout.addWidget(self.textBrowser_4, 3, 0, 1, 1)
        # self.textBrowser_6 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        # self.gridLayout.addWidget(self.textBrowser_6, 1, 0, 1, 1)
        # self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        # self.gridLayout.addWidget(self.textBrowser, 5, 0, 1, 1)
        # self.textBrowser_2 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        # self.gridLayout.addWidget(self.textBrowser_2, 5, 1, 1, 1)
        # self.textBrowser_3 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        # self.gridLayout.addWidget(self.textBrowser_3, 4, 0, 1, 1)
        # self.textBrowser_5 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        # self.gridLayout.addWidget(self.textBrowser_5, 2, 0, 1, 1)
        # self.textBrowser_7 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_7.setObjectName(_fromUtf8("textBrowser_7"))
        # self.gridLayout.addWidget(self.textBrowser_7, 0, 0, 1, 1)
        # self.textBrowser_8 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_8.setObjectName(_fromUtf8("textBrowser_8"))
        # self.gridLayout.addWidget(self.textBrowser_8, 1, 1, 1, 1)
        # self.textBrowser_9 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_9.setObjectName(_fromUtf8("textBrowser_9"))
        # self.gridLayout.addWidget(self.textBrowser_9, 2, 1, 1, 1)
        # self.textBrowser_10 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_10.setObjectName(_fromUtf8("textBrowser_10"))
        # self.gridLayout.addWidget(self.textBrowser_10, 3, 1, 1, 1)
        # self.textBrowser_11 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_11.setObjectName(_fromUtf8("textBrowser_11"))
        # self.gridLayout.addWidget(self.textBrowser_11, 4, 1, 1, 1)
        # self.textBrowser_12 = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        # self.textBrowser_12.setObjectName(_fromUtf8("textBrowser_12"))
        # self.gridLayout.addWidget(self.textBrowser_12, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)

        self.createBtns(Erasmus)
        self.createTextBrowser(Erasmus)
        self.retranslateUi(Erasmus)

        QtCore.QMetaObject.connectSlotsByName(Erasmus)

    def createBtns(self,Erasmus):
        self.countries=[] #Create empty list
        afile=open('countries.txt','r') #Open file for reading
        for line in afile: #iterate through file and add each item to the list
             self.countries.append(str(line).rstrip('\n'))
        afile.close()
        self.btns = {}
        i=1;
        for country in self.countries:
            self.btns[i] = QtGui.QPushButton(self.scrollAreaWidgetContents)
            self.btns[i].setObjectName(_fromUtf8(country))
            self.verticalLayout.addWidget(self.btns[i])
            self.btns[i].setText(_translate("Erasmus", country, None))
            i = i + 1

    def createTextBrowser(self,Erasmus):
        self.university=[]
        afile=open('Austria/university.txt','r')
        for line in afile: #iterate through file and add each item to the list
             self.university.append(str(line).rstrip('\n'))
        afile.close()

        self.textBrowser = {}
        i=0
        for row in range(0,5):
            for col in range(0,2):
                print("Row: ", row ,"Col: ", col)
                self.textBrowser[i] = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
                self.textBrowser[i].setObjectName(_fromUtf8("textBrowser"))
                self.gridLayout.addWidget(self.textBrowser[i], row, col, 1, 1)
                i +=1


    def retranslateUi(self, Erasmus):

        Erasmus.setWindowTitle(_translate("Erasmus", "Erasmus", None))
        i=0
        for row in range(0,5):
            for col in range(0,2):
                self.textBrowser[i].setHtml(_translate("Erasmus", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">" + self.university[i] + "</span></p>\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
                i +=1

        #self.pushButton_5.setText(_translate("Erasmus", countries[coutry], None))
        # self.pushButton_5.setText(_translate("Erasmus", coutries[3], None))
        # self.pushButton_4.setText(_translate("Erasmus", "PushButton", None))
        # self.pushButton_3.setText(_translate("Erasmus", "PushButton", None))
        # self.pushButton_2.setText(_translate("Erasmus", "PushButton", None))
        # self.pushButton.setText(_translate("Erasmus", "PushButton", None))
#         self.textBrowser_7.setHtml(_translate("Erasmus", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">" + countries[2] + "</span></p>\n"
# "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Erasmus = QtGui.QWidget()
    ui = Ui_Erasmus()
    ui.setupUi(Erasmus)
    Erasmus.show()
    sys.exit(app.exec_())
