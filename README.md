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

### PDI - Power Distance Index 

"Extent to which less powerful members of institutions and organizations accept that power is distributed unequally
" 

**High power distance countries** (autocratic)
People more likely to simply obey the orders of their superiors without discussion, centralized and tall organization structures

**Low power distance countries** (democratic)
Flatter and decentralized organization structures, smaller ratio of supervisors
*Geert Hofstede*

![](http://i.imgur.com/v4KG0j6.png)

What I’ve taken from Hofstede’s research above, with regards to Power Distance Index, is that we see a striking resemblance, or opposites depending on how you look at it, to my previous insight of Uncertainty Avoidance.
On first glance, there’s a shock to see Germany so low. Why do people accept that there is power inequality that the power lies with the majority, the favoured few. But in reality, the index does show us the countries that are more than happy to accept that the police have a certain ruling, and are able/allowed to invoke this authority.
What does this mean for UI design? Well gaining trust for low scoring countries is of high importance. This is done with the simple and similar UI layout. The repetitiveness allows for recognising, rather than recall.

### UAI - Uncertainty Avoidance

"Extent to which people feel threatened by ambiguous situations and have created beliefs and institutions that try to avoid such situations"

**High uncertainty avoidance countries**
People have high need for security, strong belief in experts and their knowledge, structured organizational activities, more written rules, less risk taking by managers

***Low uncertainty avoidance countries**
People are more willing to  accept risks associated with the unknown, less structured organizational activities, fewer written rules, more risk taking by managers, higher employee turnover, more ambitious employees
*Geert Hofstede*

![](http://i.imgur.com/VqUT9qc.png)

What I’ve taken from Hostede’s research above, with regards to Uncertainty Avoidance, is that there may be a few anomalies with the results seen above. Most notably the two countries scoring lower on the index. We, as Westerns, see China as being a very strict and power orientated. I discuss this below in PDI, but here, we see China scoring the lowest. 

But upon further research, we can see that China fall correctly into this position. Why? China are renowned for their for-planning, their ability to plan ahead, and always having a long term plan. This is how I see Hofstede’s Dimension scoring China so low.
As for designing for the opposite end, high Uncertainty Avoidance, the need to be able to balance different options against each other is necessary in order to make a reliable decision. I achieved this through the side to side layout between the Country selection and College options. This familiar design follows throughout the whole app.

