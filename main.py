#!/usr/bin/env python3

import sys
import time
from stepper import Controller
from pic import Ui_MotorControl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic



controle = Controller()
motorGUI = Ui_MotorControl()

class MotorControllerApp:
    def __init__(self, argv):
        self.app = QtWidgets.QApplication(argv)
        self.picDialog = QtWidgets.QDialog()
        self.ui = Ui_MotorControl()
        ui = self.ui

        ui.setupUi(self.picDialog)

        # Setup here
        ui.stepcontroller.valueChanged.connect(self.stepCount)
        ui.stepcontroller.valueChanged.connect(self.mainControl)
        ui.speedcontrol.valueChanged.connect(self.speedCalculator)
        ui.speedcontrol.valueChanged.connect(self.mainControl)
        ui.sequenceselector.valueChanged.connect(self.mainControl)
        ui.move.clicked.connect(self.activate)

    def activate(self):
        valarr =self.mainControl()
        Seq = controle.seqSetting(valarr[0])
        ui.progressBar.setMaximum(valarr[1])
        ui.progressBar.setValue(0)
        controle.mainLoop(Seq, abs(valarr[2])/1000 , abs(valarr[2])/valarr[2], valarr[1], lambda step: ui.progressBar.setValue(step))

    def show(self):
        return self.picDialog.show()

    def exec(self):
        self.app.exec_()

    def mainControl(self):
        ui = self.ui
        seqNum = ui.sequenceselector.value()
        stepNum = ui.stepcontroller.value()
        speedNum = ui.speedcontrol.value()
        return [seqNum, stepNum, speedNum]

    def stepCount(self):
        ui = self.ui
        val = ui.stepcontroller.value()
        um = float(val) *float(7.7515)
        if self.mainControl()[0] == 0:
            msg = '%f㎛'%(um/float(2))
        else:
            msg = '%f㎛'%um
        ui.lengthUnit.setText(msg)
    def speedCalculator(self):
        ui = self.ui
        wT = ui.speedcontrol.value()
        if wT == 0:
            mesg = 'stop'
        else :
            if self.mainControl()[0] == 0 :
                speed = float(7.7515)*500/float(wT)
                mesg =  '%f㎛/s'%speed
            else:
                speed = float(7.7515)*1000/float(wT)
                mesg = '%f㎛/s'%speed
        ui.speedBar.setText(mesg)

if __name__ == "__main__":
    import sys
    motorControlApp = MotorControllerApp(sys.argv)
    motorControlApp.show()
    sys.exit(motorControlApp.exec())

