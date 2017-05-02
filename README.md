# SGM-Assignment
Git repository for my submit to Dierdre Lawless' Software for the Global Market 2


## What was used
* Atom IDE
* Anaconda
* PyQt 4
* QtDesigner
* GetText
* POedit
* Deirdre Lawless, Webcourse Matertial 

## Ellicitaion

Please see the [Google Document](https://docs.google.com/document/d/1HBMDX_PnEdM9-WUczNO4CkFHU6B9AetDvavBqfrL5JA/edit?usp=sharing "Title") for full outline of the project

## Coding

At the beigning of the moule, I initally ran into difficulties running .py Scripts using Idle. I resorted to using Continuim's [Anaconda](https://www.continuum.io/downloads), and setting up an [enviroment](https://conda.io/docs/using/envs.html) with all my relvavent packages that I required. This proved to be easier, once set up, to update and use different Python packages. 

The provided code shall still run using IDLE, once [SIP](https://www.riverbankcomputing.com/software/sip/download) and [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download) are installed, along with Python 2.5/3.6 installed and added as an enviroment variable.

## QtDesigner

![alt text](http://i.imgur.com/GxJN09I.png)

## l18n 

Below is a example of how getText.py will be able to interpet the strings to be translated. In order to traslate the text 'Single Semester', I have to wrap it inside of the following syntax, _()

```python
self.pushButton_2.setText(_translate("Form", _('Single Semester'), None))
self.pushButton.setText(_translate("Form", _('Complete Year'), None))
```

Once the above has been done with all of the strings reqruired to be tranlated. The script is ready to be passed through getText.py
The restuling output is a .pot file, included in the repository.

Next, the .pot file is opened within POedit, and the relavent langauges and translations are added.
![alt text](http://i.imgur.com/9adF1yp.png)

This results in two files, .mo and .po
The first is the machine readable file, and the latter, a human readalbe file. The layout of the files must follow a standarised convention. I went with the following, a slight adjustment.
```
Erasmus
│   Eramus.ui
│   info.txt    
│   messages.pot
|   open.py
|
└───locale
|   |
│   │
│   └───de
│       │   coutries.txt
|       |   LC_MESSAGES
|                      └───
|                      |    de.mo
|                      |    de.po
|   
│ 
```
This layout continues with multiple locals, en, fr, de, fi, etc.

## L10n - Locals

```python
def setLocal(self,Form):
        local = ['en','fr','de','fi','es','zh','yo']
        # Checking with local has been selected from combobox
        for i in range(0,7):
            if self.comboBox.currentIndex() == i:
                self.comboBoxIndex = i
                self.lng = local[i]
                break
            else:
                # Default local is set to en. Will change to work with persistant data
                self.lng = ''
                self.settings(Form)
}
```

## L10n - Languages

I simply used text files to load the college in a specific language, based on the locale set from the fron page.
These were stored in a text file, 'countries.txt', within each local folder, see above.

See below of how they were loaded, as well as a look as to how each of the button are created and object values set.

```python
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
            self.btns[i].setMinimumSize(QtCore.QSize(300,0))
            self.btns[i].setObjectName(_fromUtf8(country))
            self.verticalLayout.addWidget(self.btns[i])
            self.btns[i].setText(_translate("Erasmus", country, None))
            self.btns[i].clicked.connect(partial(self.loadFile,i,Erasmus))
            i += 1
```

## C13n

PDI - Power Distance Index 

![Alt Text](http://i.imgur.com/Efst2Wx.png)

UAI - Uncertainty Avoidance

![Alt Text](http://i.imgur.com/sSI9hOY.png)
