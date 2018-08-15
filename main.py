#!/usr/bin/env python3

import sys
import time
from stepper import Controller
from pic import Ui_MotorControl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

controle = Controller()
motorGUI = Ui_MotorControl()

class SaveFile:
    def __init__(self, file):
        self.touch(file)
        self.f = open(file, "r+")
        self.f.seek(0)

    def touch(self, file):
        f = open(file, "a")
        f.close()

    def read(self):
        self.f.seek(0)
        val = self.f.read().split(",")

        try:
            int(val[0])
            int(val[1])
        except:
            self.f.seek(0)
            self.f.write("0,0")
            val = ["0", "0"]

        class ret:
            pass

        ret.step = int(val[0])
        ret.seqset = int(val[1])

        return ret

    def write(self, step, seqset):
        self.f.seek(0)
        self.f.truncate(0)
        self.f.write("%d,%d" %(step,seqset))

    def close(self):
        self.f.close()

saveFile = SaveFile("Angle")
saveFile.read()
saveFile.close()

maxAngle = 270

class MotorControllerApp:
    def __init__(self, argv):
        self.app = QtWidgets.QApplication(argv)
        self.picDialog = QtWidgets.QDialog()
        self.ui = Ui_MotorControl()
        ui = self.ui

        ui.setupUi(self.picDialog)

        # Setup here
        ui.angleSelector.valueChanged.connect(self.stepCount)
        ui.speedControl.valueChanged.connect(self.speedCalculator)
        ui.seqSel.valueChanged.connect(self.stepChange)
        ui.move.clicked.connect(self.activate)
        ui.doAdj.clicked.connect(self.adjustment)

        saveFile = SaveFile("Angle")
        ang = saveFile.read()
        ui.angleSelector.setValue(ang.step)
        if ang.seqset==0:
            ui.angleSelector.setMaximum(int(maxAngle/360*4096))
            ui.angleSelector.setValue(ang.step)
        else:
            ui.angleSelector.setMaximum(int(maxAngle/360*2048))
            ui.angleSelector.setValue(ang.step)
        saveFile.close()

    def activate(self):
        ui = self.ui
        val = self.mainControl()
        Seq = controle.seqSetting(val.seqNum)
        print (Seq)
        seqSet = int(val.seqNum)
        newAng = int(val.angleNum)

        saveFile = SaveFile("Angle")
        state = saveFile.read()
        oldAng = state.step
        ui.progressBar.setMaximum(abs(newAng-state.step))
        ui.progressBar.setValue(0)
        try: 
            direc = abs(newAng-oldAng)/(newAng-oldAng)
        except ZeroDivisionError:
            direc = 1
        step = abs(newAng-oldAng)
        controle.mainLoop(Seq, abs(val.speedNum)/10000 , direc, step, lambda step: ui.progressBar.setValue(step))

        saveFile.write(newAng, seqSet)
        saveFile.close()

    def adjustment(self):
        ui = self.ui
        adjVal = ui.adjVlaue.toPlainText()
        saveFile = SaveFile("Angle")
        ctrlVal = self.mainControl()
        foo = ctrlVal.seqNum
        try : 
            adjVal = float(adjVal)
        except:
            adjVal = float(saveFile.read().seqset)

        if foo == 0:
            saveFile.write(int(adjVal/360*4096), foo)
            ui.angleSelector.setValue(int(adjVal/360*4096))
        else:
            ui.angleSelector.setValue(int(adjVal/360*2048))
            saveFile.write(int(adjVal/360*2048), foo)

        saveFile.close()

    def show(self):
        return self.picDialog.show()

    def exec(self):
        self.app.exec_()

    def mainControl(self):
        ui = self.ui
        seqNum = ui.seqSel.value()
        angleNum = ui.angleSelector.value()
        speedNum = ui.speedControl.value()

        class ret:
            pass

        ret.seqNum = seqNum
        ret.angleNum = angleNum
        ret.speedNum = speedNum
        return ret

    def stepCount(self):
        ui = self.ui
        val = ui.angleSelector.value()
        controlVal = self.mainControl()
        if controlVal.seqNum == 0:
            deg = float(val) *float(360)/float(4096)
            ui.angleSelector.setMaximum(3*1024)
        else:
            deg = float(val)*360/float(2048)
            ui.angleSelector.setMaximum(3*512)
        msg = "%f Deg" %deg
        ui.Deg.setText(msg)

    def stepChange(self):
        ui = self.ui
        seq = ui.seqSel.value()
        saveFile = SaveFile("Angle")
        prevstate = saveFile.read()
        prevangle = prevstate.step

        angle = ui.angleSelector.value()
        if prevstate.seqset == 0 and (seq == 1 or seq == 2):
            angle = angle / 2
            prevangle = prevangle / 2
            ui.angleSelector.setValue(angle)
            ui.angleSelector.setMaximum(int(maxAngle/360*2048))

        if (prevstate.seqset == 1 or prevstate.seqset == 2) and seq == 0:
            angle = angle * 2
            prevangle = prevangle * 2
            ui.angleSelector.setMaximum(int(maxAngle/360*4096))
            ui.angleSelector.setValue(angle)

        controle.changeStepSeq(seq)

        saveFile.write(prevangle, seq)
        saveFile.close()

    def speedCalculator(self):
        ui = self.ui
        wT = ui.speedControl.value()
        if wT == 0:
            mesg = 'stop'
        else :
            if self.mainControl().seqNum == 0 :
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

