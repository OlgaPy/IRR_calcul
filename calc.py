import inspect
import sys
import numpy
import math
from PyQt5.QtCore import pyqtSignal, Qt, pyqtSlot, QObject
from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QLineEdit, QLabel, QListView, QDialog, QTextEdit, QSlider,
                             QStackedWidget, QVBoxLayout)

class CALC(QWidget, QObject):
    # Каждое приложение должно создать объект QApplication
    # sys.argv - список аргументов командной строки
    def __init__(self):
        super().__init__()
        #self.irr()
        self.inf = [0, 3.6, 4.0, 4.0, 3.6, 3.3, 3.0, 3.1]

        self.e36 = 25.3

        self.initUI()

    @pyqtSlot()
    def setTovar(self):
        try:
            tovarNow = float(self.textboxResultTrade.text())
            count = float(self.textboxCoof.text())
            self.textboxParam1.setText(str(int(tovarNow * count)))

        except Exception as ex:
            print(ex)



    @pyqtSlot()
    def getPo(self):
        try:
            tovar = float(self.textboxParam1.text()) #b28
            invest = float(self.textboxParam3.text()) #b28
            cost = 40000000 #38
            com = float(self.textboxParam2.text())
            testIrr = float(self.textboxResult.text())
            irr = self.getIrr(tovar, com, invest, cost)
            #  test = self.getIrr(tovar, com, invest, cost)
            while ( irr <= testIrr or math.isnan(irr)):

                cost = cost - 10000
                irr = self.getIrr(tovar, com, invest, cost)

            self.textboxParam4.setText(str(cost))
            self.sliderParam4.setValue(int(cost))



        except Exception as ex:
            print(ex)


    @pyqtSlot()
    def getInvest(self):
        try:
            tovar = float(self.textboxParam1.text()) #b28
            invest = 10000000 #b28
            cost = float(self.textboxParam4.text()) #38
            com = float(self.textboxParam2.text())
            testIrr = float(self.textboxResult.text())
            irr = self.getIrr(tovar, com, invest, cost)
            #  test = self.getIrr(tovar, com, invest, cost)
            while ( irr <= testIrr or math.isnan(irr)):

                invest = invest - 10000
                irr = self.getIrr(tovar, com, invest, cost)

            self.textboxParam3.setText(str(invest))
            self.sliderParam3.setValue(int(invest))



        except Exception as ex:
            print(ex)


    @pyqtSlot()
    def getCom(self):
        try:
            tovar = float(self.textboxParam1.text()) #b28
            invest = float(self.textboxParam3.text()) #b28
            cost = float(self.textboxParam4.text()) #38
            com = 20
            testIrr = float(self.textboxResult.text())
            irr = self.getIrr(tovar, com, invest, cost)
            #  test = self.getIrr(tovar, com, invest, cost)
            while ( irr <= testIrr or math.isnan(irr)):

                com = com - 0.01
                print(com)
                irr = self.getIrr(tovar, com, invest, cost)

            print(com)
            self.textboxParam2.setText(str('{:6.2f}'.format(com)))
            self.sliderParam2.setValue(int(com))



        except Exception as ex:
            print(ex)


    @pyqtSlot()
    def getTovar(self):
        try:

            com = float(self.textboxParam2.text()) #24
            invest = float(self.textboxParam3.text()) #b28
            cost = float(self.textboxParam4.text()) #38
            tovar =1000
            testIrr = float(self.textboxResult.text())
            tovarNow = float(self.textboxResultTrade.text())
            irr = self.getIrr(tovar, com, invest, cost)
            #  test = self.getIrr(tovar, com, invest, cost)
            while ( irr <= testIrr or math.isnan(irr)):
                tovar = tovar + 100000
                irr = self.getIrr(tovar, com, invest, cost)

            self.textboxParam1.setText(str(tovar))
            self.textboxCoof.setText(str('{:6.2f}'.format(tovar/tovarNow)))
            self.sliderParam1.setValue(int(tovar))


        except Exception as ex:
            print(ex)



    def getIrr(self, tovar, com, invest, cost):

        self.yeasrsPay = []
        self.yearsHavePay = []
        self.b44 = []
        self.yearsAllPay = []
        self.pribilDoNalogo = [] #57
        self.itogo = []
        self.rbp = [cost, 0, 0, 0 , 0,0,0,0]
        tovarWithoutNds = tovar /1.1727 #19


        tovarNow = float(self.textboxResultTrade.text())

        self.textboxCoof.setText(str('{:6.2f}'.format(tovar/tovarNow)))

        self.commision =float( tovar * com/100) #b
        self.yeasrsPay.append(invest + 300000) #53
        for i in range (1, len(self.inf)):
            self.yeasrsPay.append(self.yeasrsPay[i-1]*(100+self.inf[i])/100) #53

        self.yearsHavePay.append(tovarWithoutNds) #52
        for i in range (1, len(self.inf)):
            self.yearsHavePay.append(self.yearsHavePay[i-1]*(100+self.inf[i])/100) #52


        for i in range (0, len(self.inf)):
            self.b44.append((self.yearsHavePay[i] * self.e36/100)/((100+self.e36)/100))

        for i in range (0, len(self.inf)):
            self.yearsAllPay.append((self.yearsHavePay[i]*1.1727)*com/100 + (self.yearsHavePay[i]*1.1727)*1.5/100 +
                                    ((self.yearsHavePay[i]*1.1727)*0.215/100*0.5) +((self.yearsHavePay[i]*1.1727)*3.15/100)*0.5 +
                                    (self.yearsHavePay[i] -self.b44[i])) #54

        for i in range (0, len(self.inf)):
            self.pribilDoNalogo.append(self.yearsHavePay[i] - self.yeasrsPay[i] - 0 - self.rbp[i] - self.yearsAllPay[i])#57
            self.itogo.append(self.pribilDoNalogo[i] - self.pribilDoNalogo[i]*0.2)

        #       print (self.yeasrsPay)
        #  print (self.yearsHavePay)
        #  print (self.b44)
        print(self.itogo)
        return self.irr(self.itogo)

    @pyqtSlot()
    def getIrrSlot(self):
        try:
            self.yeasrsPay = []
            self.yearsHavePay = []
            self.b44 = []
            self.yearsAllPay = []
            self.pribilDoNalogo = [] #57
            self.itogo = []

            tovar = float(self.textboxParam1.text()) #18
            com = float(self.textboxParam2.text()) #24
            invest = float(self.textboxParam3.text()) #b28
            cost = float(self.textboxParam4.text()) #38
            self.textboxResult.setText(str('{:6.2f}'.format(self.getIrr(tovar, com, invest, cost))))
        except Exception as ex:
            self.textboxResult.setText("Error")
            print(ex)

    @pyqtSlot(int)
    def setParam1(self, param1):
        self.textboxParam1.setText(str(param1))

    @pyqtSlot(int)
    def setParam2(self, param2):
        self.textboxParam2.setText(str(param2))

    @pyqtSlot(int)
    def setParam3(self, param3):
        self.textboxParam3.setText(str(param3))

    @pyqtSlot(int)
    def setParam4(self, param4):
        self.textboxParam4.setText(str(param4))

    @pyqtSlot(int)
    def setParam5(self, param5):
        self.textboxResult.setText(str(param5))

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        leftBox = 200
        param1 = QLabel(self)
        param1.move(20, 20)
        param1.setText("Trade Turnover")
        param1.show()

        self.textboxParam1 = QLineEdit(self)
        self.textboxParam1.move(leftBox, 20)
        self.textboxParam1.resize(180, 30)
        self.textboxParam1.setText(str(132525984))

        self.textboxParam1.textChanged.connect(self.getIrrSlot)


        self.sliderParam1 = QSlider( Qt.Horizontal, self)
        self.sliderParam1.setGeometry(400, 20, 300, 30)
        self.sliderParam1.setMinimum(44175328)
        self.sliderParam1.setMaximum(441753280)
        self.sliderParam1.setTickInterval(10000)
        self.sliderParam1.setSingleStep(1)
        self.sliderParam1.show()
        self.sliderParam1.valueChanged[int].connect(self.setParam1)

        self.buttonTovar = QPushButton(self)
        self.buttonTovar.move(750, 20)
        self.buttonTovar.resize(120, 30)
        self.buttonTovar.setText("get T. T.")
        self.buttonTovar.clicked.connect(self.getTovar)



        param2 = QLabel(self)
        param2.move(20, 100)
        param2.setText("% Commission")
        param2.show()

        self.textboxParam2 = QLineEdit(self)
        self.textboxParam2.move(leftBox, 100)
        self.textboxParam2.resize(180, 30)
        self.textboxParam2.setText(str(10))
        self.textboxParam2.textChanged.connect(self.getIrrSlot)

        self.sliderParam2 = QSlider(Qt.Horizontal, self)
        self.sliderParam2.setGeometry(400, 100, 300, 30)
        self.sliderParam2.setMinimum(1)
        self.sliderParam2.setMaximum(100)
        self.sliderParam2.setTickInterval(1)
        self.sliderParam2.setSingleStep(1)
        self.sliderParam2.show()
        self.sliderParam2.valueChanged[int].connect(self.setParam2)

        self.buttonCom= QPushButton(self)
        self.buttonCom.move(750, 100)
        self.buttonCom.resize(120, 30)
        self.buttonCom.setText("get % C.")
        self.buttonCom.clicked.connect(self.getCom)


        param3 = QLabel(self)
        param3.move(20, 180)
        param3.setText("Marketing Investments")
        param3.show()

        self.textboxParam3 = QLineEdit(self)
        self.textboxParam3.move(leftBox, 180)
        self.textboxParam3.resize(180, 30)
        self.textboxParam3.setText(str(3000000))
        self.textboxParam3.textChanged.connect(self.getIrrSlot)

        self.sliderParam3 = QSlider(Qt.Horizontal, self)
        self.sliderParam3.setGeometry(400, 180, 300, 30)
        self.sliderParam3.setMinimum(100000)
        self.sliderParam3.setMaximum(10000000)
        self.sliderParam3.setValue (600000)
        self.sliderParam3.setSingleStep(10000)
        self.sliderParam3.show()
        self.sliderParam3.valueChanged[int].connect(self.setParam3)

        self.buttonInv= QPushButton(self)
        self.buttonInv.move(750, 180)
        self.buttonInv.resize(120, 30)
        self.buttonInv.setText("get M. I.")
        self.buttonInv.clicked.connect(self.getInvest)

        param4 = QLabel(self)
        param4.move(20, 260)
        param4.setText("Cost of SoftWare")
        param4.show()

        self.textboxParam4 = QLineEdit(self)
        self.textboxParam4.move(leftBox, 260)
        self.textboxParam4.resize(180, 30)
        self.textboxParam4.setText(str(9000000))
        self.textboxParam4.textChanged.connect(self.getIrrSlot)

        self.sliderParam4 = QSlider(Qt.Horizontal, self)
        self.sliderParam4.setGeometry(400, 260, 300, 30)
        self.sliderParam4.setMinimum(500000)
        self.sliderParam4.setMaximum(15000000)
        self.sliderParam4.setTickInterval(100000)
        self.sliderParam4.setSingleStep(100000)
        self.sliderParam4.show()
        self.sliderParam4.valueChanged[int].connect(self.setParam4)

        self.buttonPo= QPushButton(self)
        self.buttonPo.move(750, 260)
        self.buttonPo.resize(120, 30)
        self.buttonPo.setText("get C. SW")
        self.buttonPo.clicked.connect(self.getPo)

        result = QLabel(self)
        result.move(20, 340)
        result.setText("IRR")
        result.show()

        self.textboxResult = QLineEdit(self)
        self.textboxResult.move(leftBox, 340)
        self.textboxResult.resize(180, 30)
        self.textboxResult.setText("")

        self.sliderParam5 = QSlider(Qt.Horizontal, self)
        self.sliderParam5.setGeometry(400, 340, 300, 30)
        self.sliderParam5.setMinimum(0)
        self.sliderParam5.setMaximum(100)
        self.sliderParam5.setTickInterval(1)
        self.sliderParam5.setSingleStep(1)
        self.sliderParam5.show()
        self.sliderParam5.valueChanged[int].connect(self.setParam5)

        self.buttonIrr= QPushButton(self)
        self.buttonIrr.move(750, 340)
        self.buttonIrr.resize(120, 30)
        self.buttonIrr.setText("IRR")
        self.buttonIrr.clicked.connect(self.getIrrSlot)



        trade = QLabel(self)
        trade.move(20, 440)
        trade.setText("Now Trade Turnover")
        trade.show()

        self.textboxResultTrade = QLineEdit(self)
        self.textboxResultTrade.move(leftBox, 440)
        self.textboxResultTrade.resize(180, 30)
        self.textboxResultTrade.setText(str(44175328))
        self.textboxResultTrade.textEdited.connect(self.setTovar)

        tradeCouny = QLabel(self)
        tradeCouny.move(400, 440)
        tradeCouny.setText("Multiplier of Now T.T.")
        tradeCouny.show()

        self.textboxCoof = QLineEdit(self)
        self.textboxCoof.move(520, 440)
        self.textboxCoof.resize(40, 30)
        self.textboxCoof.setText(str(3))
        self.textboxCoof.textEdited.connect(self.setTovar)


        self.setMinimumSize(600, 400)

        self.setGeometry(100, 100, 900, 500)
        self.setWindowTitle('Payback calculation')
        self.show()



    def irr(self, data):

        #        print(round(numpy.irr([-5561539, 1697446, 1765344, 1835958, 1902052, 1964820, 2023764, 2086501]), 4)*100)
        return  (round(numpy.irr(data), 4)*100)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = CALC()
    sys.exit(app.exec_())
