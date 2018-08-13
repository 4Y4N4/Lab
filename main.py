#!/usr/bin/env python3

import sys
import time
from stepper import Controller
from pic import Ui_MotorControl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic



controle = Controller()
motorGUI = Ui_MotorControl()
try:
    f = open("Angle", "r")
except FileNotFoundError :
    f = open("Angle", "w")
    f.write("0,0")
    #(angle,seq)
finally:
    f.close()

class MotorControllerApp:
    def __init__(self, argv):
        self.app = QtWidgets.QApplication(argv)
        self.picDialog = QtWidgets.QDialog()
        self.ui = Ui_MotorControl()
        ui = self.ui

        ui.setupUi(self.picDialog)

        # Setup here
        ui.angleSelector.valueChanged.connect(self.stepCount)
        ui.angleSelector.valueChanged.connect(self.mainControl)
        ui.speedControl.valueChanged.connect(self.speedCalculator)
        ui.speedControl.valueChanged.connect(self.mainControl)
        ui.seqSel.valueChanged.connect(self.mainControl)
        ui.move.clicked.connect(self.activate)
        ui.adjVlaue.textChanged.connect(self.adjustment)
        ui.doAdj.clicked.connect(self.adjustment)
        f =open("Angle","r")
        Ang = f.read().split(",")
        ui.angleSelector.setValue(int(float(Ang[0])))
        maxAngle = 270
        if int(Ang[1])==0:
            ui.angleSelector.setMaximum(int(maxAngle/360*4096))
            ui.angleSelector.setValue(int(Ang[0]))
        else:
            ui.angleSelector.setMaximum(int(maxAngle/360*2048))
            ui.angleSelector.setValue(int(Ang[0]))
        f.close()



    def activate(self):
        ui = self.ui
        valarr = self.mainControl()
        Seq = controle.seqSetting(valarr[0])
        print (Seq)
        seqSet = int(valarr[0])
        newAng = int(valarr[1])
        f = open("Angle","r")
        stateArr = f.read().split(",")
        oldAng = int(stateArr[0])
        ui.progressBar.setMaximum(abs(newAng-int(stateArr[0])))
        ui.progressBar.setValue(0)
        if int(stateArr[1]) == seqSet:
            try: 
                direc = abs(newAng-oldAng)/(newAng-oldAng)
            except ZeroDivisionError:
                direc = 1
            step = abs(newAng-oldAng)
            controle.mainLoop(Seq, abs(valarr[2])/10000 , direc, step, lambda step: ui.progressBar.setValue(step))
        elif (int(stateArr[1]) == 0):
            try:
                direc = abs(newAng-oldAng)/(newAng-oldAng)
            except ZeroDivisionError:
                direc = 1
            step = (newAng-oldAng)
            controle.mainLoop(Seq, abs(valarr[2])/10000 , direc, step, lambda step: ui.progressBar.setValue(step))
        elif (int(seqSet) ==0):
            try:
                direc = abs(newAng-oldAng)/(newAng-oldAng)
            except ZeroDivisionError:
                direc = 1
            step = abs(newAng-oldAng)
            controle.mainLoop(Seq, abs(valarr[2])/10000, direc, step, lambda step: ui.progressBar.setValue(step))
        else:
            try:
                direc = abs(newAng-oldAng)/(newAng-oldAng)
            except ZeroDivisionError:
                direc = 1
            step = abs(newAng-oldAng)
            controle.mainLoop(Seq, abs(valarr[2])/10000, direc, step, lambda step: ui.progressBar.setValue(step))

        #need to rebuild #
        f.close()
        Angle = int(valarr[1])
        f = open("Angle","w")
        f.write("%d,%d" %(step,seqSet))
        f.close()

    def adjustment(self):
        ui = self.ui
        adjVal = ui.adjVlaue.toPlainText()
        f = open("Angle","w")
        fooArr = self.mainControl()
        foo = fooArr[0]
        try : 
            float(adjVal)
        except:
            adjVal = f.read()
        if foo == 0:
            f.write("%d,%d" %(int(float(adjVal)/360*4096),foo))
            ui.angleSelector.setValue(int(float(adjVal)/360*4096))
                
        else:
            ui.angleSelector.setValue(int(float(adjVal)/360*2048))
            f.write("%d,%d" %(int(float(adjVal)/360*2048),foo))
        f.close()
    def show(self):
        return self.picDialog.show()

    def exec(self):
        self.app.exec_()

    def mainControl(self):
        ui = self.ui
        seqNum = ui.seqSel.value()
        angleNum = ui.angleSelector.value()
        speedNum = ui.speedControl.value()
        return [seqNum, angleNum, speedNum]

    def stepCount(self):
        ui = self.ui
        val = ui.angleSelector.value()
        arrArr = self.mainControl()
        if arrArr[0] == 0:
            deg = float(val) *float(360)/float(4096)
            ui.angleSelector.setMaximum(3*1024)
        else:
            deg = float(val)*360/float(2048)
            ui.angleSelector.setMaximum(3*512)
        msg = "%f Deg" %deg
        ui.Deg.setText(msg)
        

    def speedCalculator(self):
        ui = self.ui
        wT = ui.speedControl.value()
        if wT == 0:
            mesg = 'stop'
        else :
            if self.mainControl()[0] == 0 :
                speed = float(360)/float(2048)/float(wT)*10000
                mesg =  '%f Deg/s'%speed
            else:
                speed = float(360)/float(4096)/float(wT)*10000
                mesg = '%fDeg/s'%speed
        ui.speed.setText(mesg)

if __name__ == "__main__":
    import sys
    motorControlApp = MotorControllerApp(sys.argv)
    motorControlApp.show()
    sys.exit(motorControlApp.exec())

