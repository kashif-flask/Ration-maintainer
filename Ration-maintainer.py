


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.gridLayout_2.addWidget(self.calendarWidget_2, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 3, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rashan Maintainer"))
        MainWindow.setWindowIcon(QtGui.QIcon("app.png"))
        self.label.setText(_translate("MainWindow", "Item"))
        self.label_2.setText(_translate("MainWindow", "Quantity"))
        self.label_3.setText(_translate("MainWindow", "Rate"))
        self.label_5.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rate"))
        self.label_6.setText(_translate("MainWindow", "Total"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton.setIcon(QtGui.QIcon("save.png"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete row"))
        self.pushButton_2.setIcon(QtGui.QIcon("del.png"))
        
        self.paintCell()

        self.msg=QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setWindowTitle("Error!")
        self.msg.setText("Quantity and Rate should be numeric")
        self.msg1=QtWidgets.QMessageBox()
        self.msg1.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg1.setWindowTitle("Error!")
        self.msg1.setText("Fill all quantities before submiting!")


        self.calendarWidget_2.clicked.connect(self.fn)
        self.lineEdit.textEdited.connect(lambda:self.f1(self.lineEdit))
        self.lineEdit_2.textEdited.connect(lambda:self.f2(self.lineEdit_2))
        self.lineEdit_3.textEdited.connect(lambda:self.f3(self.lineEdit_3))
        self.pushButton.clicked.connect(self.ad)
        self.pushButton_2.clicked.connect(self.rmv)
        self.tableWidget.itemClicked.connect(self.chn)
    
    def fn(self):
        try:
            self.date=self.calendarWidget_2.selectedDate().toString()
            self.lineEdit_4.setText(self.date)
            self.tableWidget.setRowCount(0)
            with open("rasan.json",'r') as f:
                self.dic=json.load(f)
            res=not self.dic
            if not res and self.date in self.dic.keys():
                l=len(self.dic[self.date]["Item"])
                keys=["Item","Quantity","Rate"]
                
                for i in range(l):
                    self.val1=str(self.dic[self.date]["Item"][i])
                    self.val2=str(self.dic[self.date]["Quantity"][i])
                    self.val3=str(self.dic[self.date]["Rate"][i])
                    
                    rowPosition=self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    
            
                    self.tableWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(self.val1))
            
                    self.tableWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(self.val2))
                    
                    self.tableWidget.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(self.val3))
                self.tot()
            else:
                self.label_6.setText("Total=0")
        except Exception as e:
            print(str(e))
        
    def f1(self,l):
        try:
            l.setText(l.text())
            self.item=l.text()
        except Exception as e:
            pass
        

    def f2(self,l):
        try:
            l.setText(l.text())
            
            try:
                n=float(l.text())
                self.quantity=l.text()
            except:
                self.msg.exec_()
                
        except Exception as e:
            pass
    def f3(self,l):
        try:
            l.setText(l.text())
            
            try:
                n=float(l.text())
                self.rate=l.text()
            except:
                self.msg.exec_()
        except Exception as e:
            pass

    def chn(self):
        try:
            self.tableWidget.itemChanged.connect(lambda:self.ed(self.tableWidget.currentRow(),self.tableWidget.currentColumn()))
        except Exception as e:
            pass
    

    def ed(self,row,col):
        try:
            v=self.tableWidget.currentItem().text()
            try:
                if col!=0:
                    n=float(v)
                keys=["Item","Quantity","Rate"]
                with open("rasan.json",'r') as f:
                    self.dic=json.load(f)
                self.dic[self.date][keys[col]][row]=v
                self.tot()
                with open("rasan.json","w") as f:
                    json.dump(self.dic,f)
            except:
                self.msg.exec_()
            
        except Exception as e:
            pass
        
    def tot(self):
        try:
            row=self.tableWidget.rowCount()
            
            t=0
            for i in range(row):
                
                t=t+float(self.tableWidget.item(i,1).text())*float(self.tableWidget.item(i,2).text())
            self.label_6.setText(f"Total={t}")
        except Exception as e:
            pass
    def rmv(self):
        try:
            index=self.tableWidget.selectedIndexes()[0]
            
            self.tableWidget.removeRow(index.row())
            with open("rasan.json",'r') as f:
                self.dic=json.load(f)
            self.dic[self.date]["Item"].pop(index.row())
            self.dic[self.date]["Quantity"].pop(index.row())
            self.dic[self.date]["Rate"].pop(index.row())
            self.tot()
            
            with open("rasan.json",'w') as f:
                json.dump(self.dic,f)
            self.paintCell()

        except Exception as e:
            print(str(e))

    def paintCell(self):
        
        with open("rasan.json",'r') as f:
                self.dic=json.load(f)
        for date in self.dic:
            
            if len(self.dic[date]["Item"])>0:
                format=QTextCharFormat()
                format.setFont(QFont('Times',15))
                self.calendarWidget_2.setDateTextFormat(QDate.fromString(date),format)
            else:
                format=QTextCharFormat()
                format.setFont(QFont('Times',10))
                self.calendarWidget_2.setDateTextFormat(QDate.fromString(date),format)
                
           
            


    def ad(self):
        try:
            
            rowPosition=self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            
            with open("rasan.json",'r') as f:
                self.dic=json.load(f)
            if self.date in self.dic.keys():
                print(self.date)
                print(self.item,self.quantity,self.rate)
                d1=self.dic[self.date]["Item"]
                d1.append(self.item)
                d2=self.dic[self.date]["Quantity"]
                d2.append(self.quantity)
                d3=self.dic[self.date]["Rate"]
                d3.append(self.rate)
                self.dic[self.date]={"Item":d1,"Quantity":d2,"Rate":d3}
            else:
                print(self.item,self.quantity,self.rate)
                self.dic[self.date]={"Item":[self.item],"Quantity":[self.quantity],"Rate":[self.rate]}

            self.tableWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(self.item))
            self.tableWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(self.quantity))
            self.tableWidget.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(self.rate))
            self.tot()
            
            with open("rasan.json",'w') as f:
                json.dump(self.dic,f)
            self.paintCell()
            
                
        except Exception as e:
            self.msg1.exec_()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
