# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openWindowsuiComboBoxLng.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from functools import partial
import gettext

# Declaring the font type that will be used
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

class Ui_Erasmus(QtGui.QWidget):
    def __init__(self,lng,parent = None):
        super(Ui_Erasmus, self).__init__(parent)
        self.lng = lng
        self.setupUi(self,lng)


    def setupUi(self, Erasmus,lng):
        # Setting up the secondary Ui
        Erasmus.setObjectName(_fromUtf8("Erasmus"))
        Erasmus.resize(1458,1000)
        self.horizontalLayout = QtGui.QHBoxLayout(Erasmus)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(Erasmus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollArea.setMaximumSize(QtCore.QSize(400,16777215))
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

        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        # Calling all the secondary funtions
        self.createBtns(Erasmus)
        self.createTextBrowser(Erasmus)
        self.loadFile(1,Erasmus)

        QtCore.QMetaObject.connectSlotsByName(Erasmus)

    # Setting up the buttons as part of the secondary Ui
    def createBtns(self,Erasmus):
        self.countries=[] #Create empty list
        afile=open('locale/' + self.lng + '/countries.txt','r',encoding="utf8") #Open file for reading and with correct character encoding
        for line in afile: #iterate through file and add each item to the list
             self.countries.append(str(line).rstrip('\n'))
        afile.close()
        self.btns = {}
        i=1;
        self.btns[0] = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btns[0].setObjectName(_fromUtf8("exit"))
        self.verticalLayout.addWidget(self.btns[0])
        self.btns[0].setText(_translate("Form", _('Exit'), None))
        self.btns[0].clicked.connect(self.closeIt)
        for country in self.countries:
            self.btns[i] = QtGui.QPushButton(self.scrollAreaWidgetContents)
            self.btns[i].setObjectName(_fromUtf8(country))
            self.verticalLayout.addWidget(self.btns[i])
            self.btns[i].setText(_translate("Erasmus", country, None))
            self.btns[i].clicked.connect(partial(self.loadFile,i,Erasmus))
            i += 1



    # Setting up the text browsers as part of the secondary Ui
    def createTextBrowser(self,Erasmus):

        self.textBrowser = {}
        i=0
        for row in range(0,6):
            for col in range(0,2):
                self.textBrowser[i] = QtGui.QLabel(self.scrollAreaWidgetContents_2)
                self.textBrowser[i].setMinimumSize(QtCore.QSize(250,100))
                self.textBrowser[i].setAlignment(QtCore.Qt.AlignCenter)
                self.textBrowser[i].setObjectName("textBrowser" + str(i))
                self.textBrowser[i].setFrameShape(QtGui.QFrame.WinPanel)
                self.gridLayout.addWidget(self.textBrowser[i], row, col, 1, 1)

                i +=1



    def showText1(self):
        print ("Label 1 clicked")
    # Populating the text browsers
    def retranslateUi(self, Erasmus):

        Erasmus.setWindowTitle(_translate("Erasmus", "Erasmus", None))

        self.textBrowser[0].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[1].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[2].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[3].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[4].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[5].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[6].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[7].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[8].mouseReleaseEvent=lambda event:self.secondView(Erasmus)
        self.textBrowser[9].mouseReleaseEvent=lambda event:self.secondView(Erasmus)

        i=0
        for row in range(0,6):
            for col in range(0,2):
                self.textBrowser[i].setText(_translate("Erasmus",self.university[i],None))

                #self.textBrowser[i].setHtml(_translate("Erasmus", '''<html><body><a href="some_special_identifier://a_function">'''+ self.university[i] +'''</a><br/></body></html''', None))

                # <a href="some_special_identifier://a_function">
                # (_translate("Erasmus", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                # "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                # "p, li { white-space: pre-wrap; }\n"
                # "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                # "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">" + self.university[i] + "</span></p>\n"
                # "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))

                i +=1

    # Populating all the relevant lists
    def loadFile(self,count,Erasmus):
        # self.countries=[] #Create empty list
        # afile=open('countries.txt','r') #Open file for reading
        # for line in afile: #iterate through file and add each item to the list
        #     self. countries.append(str(line).rstrip('\n'))
        # afile.close()
        print(count)
        self.info=[]
        afile=open("info.txt",'r')
        for line in afile:
            self.info.append(str(line).rstrip('\n'))
        afile.close()

        countryList = ['Austria','Belgium','China','Czech','Denmark','Finland','Germany','Italy','Netherland','Norway','SKorea']

        self.university=[]
        afile=open('University/' + countryList[count-1] + '/eng.txt','r')
        for line in afile: #iterate through file and add each item to the list
             self.university.append(str(line).rstrip('\n'))
        afile.close()
        self.retranslateUi(Erasmus)


    def secondView(self,Erasmus):
         i=0
         for uni in self.university:
             self.btns[i+1].setText(_translate("Erasmus", uni, None))
             i+=1
         j=0
         for info in self.info:
             self.textBrowser[j].setText(_translate("Erasmus",info,None))
             j+=1

    def closeIt(self):
        self.close()

class Ui_Open(QtGui.QWidget):
    def __init__(self,parent = None):
        super(Ui_Open, self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, Form):
        # Setting up the UI
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1458, 1000)
        Form.setMaximumSize(QtCore.QSize(1458, 1000))
        self.styledata=' '
        file=open('css/style.css','r')
        self.styledata=file.read()
        file.close()
        self.setStyleSheet(self.styledata)
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
        self.pushButton_2.setObjectName(_fromUtf8("singleSem"))
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

        # Calling all the secondary funtions
        self.setLocal(Form)
        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        # self.pushButton_2.clicked.connect(partial(self.on_pushButton_clicked))
        # self.pushButton.clicked.connect(partial(self.on_pushButton_clicked))
        # Full year button. With a connected function
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # Launching the second window
    def on_pushButton_clicked(self):
        dialog = Ui_Erasmus(self.lng)
        dialog.show()

    # Adding titles where neccessary
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", _('Single Semester'), None))
        self.pushButton.setText(_translate("Form", _('Complete Year'), None))
        self.comboBox.addItems(["English","Français","Deutsch","Suomi","Español","中文","Èdè Yorùbá"])
        self.comboBox.currentIndexChanged.connect(self.setLocal)
        self.numOfElements = self.comboBox.count()


    def setLocal(self,Form):
        local = ['en','fr','de','fi','es','zh','yo']
        # Checking with local has been selected from combobox
        for i in range(0,7):
            if self.comboBox.currentIndex() == i:
                self.lng = local[i]
                break
            else:
                # Default local is set to en. Will change to work with persistant data
                self.lng = 'en'
        langtouse = gettext.translation(self.lng, localedir='locale', languages=[self.lng])
        langtouse.install()
        print("We're set to", self.lng)
        self.pushButton_2.setText(_translate("Form", _('Single Semester'), None))
        self.pushButton.setText(_translate("Form", _('Complete Year'), None))




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    main = Ui_Open()
    main.show()
    sys.exit(app.exec_())
