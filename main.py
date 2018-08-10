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
    f.open("Angle", "r")
except FileNotFoundError :
    f.open("Angle", "w")
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
        ui.angleSelector.valueChanger.connect(self.activate)
        ui.speedControl.valueChanged.connect(self.speedCalculator)
        ui.speedControl.valueChanged.connect(self.mainControl)
        ui.seqSel.valueChanged.connect(self.mainControl)
        ui.move.clicked.connect(self.activate)
        ui.adjValue.textChanged.connect(self.adjustment)
        ui.doAdj.clicked.connect(self.adjustment)
        f.open("Angle","r")
        Ang = f.read().split(",")
        ui.angleSelector.setvalue(int(Ang[0]))
        maxAngle = 270
        if int(Ang[1])==0:
            ui.angleselector.setMaximum(int(maxAngle/360*4096))
            ui.angleSelector.setValue(int(Ang[0]))
        else:
            ui.angleselector.setMaximum(int(maxangle/360*2048))
            ui.angleSelector.setValue(int(Ang[0]))
        f.close()



    def activate(self):
        ui = self.ui
        valarr = self.mainControl()
        Seq = controle.seqSetting(valarr[0])
        seqSet = int(valarr[0])
        newAng = int(valarr[1])
        ui.progressBar.setMaximum(valarr[1])
        ui.progressBar.setValue(0)
        f.open("Angle","r")
        stateArr = f.read().split(",")
        oldAng = int(stateArr[0])
        if int(stateArr[1]) == seqSet:
            direc = abs(newAng-oldAng)/(newAng-oldAng)
            step = abs(newAng-oldAng)
            controle.mainLoop(Seq, abs(valarr[2])/1000 , direc, step, lambda step: ui.progressBar.setValue(step))
        elif (int(stateArr[1]) == 0):
            direc = abs(newAng-(oldAng/2))/(newAng-(oldAng/2))
            step = abs(int(newAng-oldAng/2))
            controle.mainLoop(Seq, abs(valarr[2])/1000 , direc, step, lambda step: ui.progressBar.setValue(step))
        else:
            direc = abs(newAng-(oldAng*2))/(newAng-(oldAng*2))
            step = abs(newAng-(oldAng*2))
            controle.mainloop(Seq, abs(vallarr[2])/1000, direc, step, lambda step: ui.progressBar.setValue(step))
        #need to rebuild #
        f.close
        Angle = int(valarr[1])
        f.open("Angle","w")
        f.write("%d,%d" %(Angle,seqSet))
        f.close

    def adjustment(self):
        ui = self.ui
        adjVal = int(ui.adjValue.text())
        f.open("Angle","w")
        fooArr = self.mainControl()
        foo = fooArr[0]
        if foo == 0:
            f.write("%f,%f" %(int(float(adjVal))/4096*360,foo))
        else:
            f.write("%f,%f" %(int(float(adjVal)/2048*360),foo))
        f.colse()

    def show(self):
        return self.picDialog.show()

    def exec(self):
        self.app.exec_()

    def mainControl(self):
        ui = self.ui
        seqNum = ui.seqSel.value()
        angleNum = ui.angleSelector.value()
        speedNum = ui.speedControl.value()
        return [seqNum, anlgeNum, speedNum]

    def stepCount(self):
        ui = self.ui
        val = ui.angleSelector.value()
        Deg = float(val) *float(360)/float(2048)
        if self.mainControl()[0] == 0:
            msg = '%f Deg'%(Deg/float(2))
        else:
            msg = '%f Deg'%Deg
        ui.Deg.setText(msg)

    def speedCalculator(self):
        ui = self.ui
        wT = ui.seqSel.value()
        if wT == 0:
            mesg = 'stop'
        else :
            if self.mainControl()[0] == 0 :
                speed = float(360)/float(2048)/float(wT)
                mesg =  '%f Deg/s'%speed
            else:
                speed = float(360)/float(2048)/float(wT)
                mesg = '%fDeg/s'%speed
        ui.speed.setText(mesg)

if __name__ == "__main__":
    import sys
    motorControlApp = MotorControllerApp(sys.argv)
    motorControlApp.show()
    sys.exit(motorControlApp.exec())

