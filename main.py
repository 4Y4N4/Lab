import sys
import time
#import RPi.GPIO as GP
import stepper
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import pic
"""
GPIO.setmode(GPIO.BCM)

#physical pina are 31,33,35,37
Pins = [6,13,19,26]
for pin in Pins:
    print "setup pins"
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

controle = stepper()
"""
controle = stepper()
motorGUI = Ui_MotorControl()
class window(motorGUI, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUI(self, MotorControl)
    def mainControl(self):
        seqNum = self.sequenceselector.value()
        stepNum = self.stepcontroler.value()
        speedNum = self.speedcontrol.value()
        return [seqNum, stepNum, speedNum]

    def stepCount(self):
        val = self.stepcontroler.value()
        um = float(val) *float(7.7515)
        if self.mainControl()[0] == 0:
            msg = '%f㎛'%(um/float(2))
        else:
            msg = '%f㎛'%um
        self.lengthUnit.showMessage(msg)
 
    def speedCalculator(self):
        wT = self.speedcontrol.value()
        if wT == 0:
            mesg = 'stop'
        else :
            if self.mainControl()[0] == 0 :
                speed = float(7.7515)*500/float(wT)
                mesg =  '%f㎛/s'%speed
            else:
                speed = float(7.7515)*1000/float(wT)
                mesg = '%f㎛/s'%speed
        self.speedBar.showMessage(mesg)

    def retranslateUi(self, MotorControl):
        _translate = QtCore.QCoreApplication.translate
        MotorControl.setWindowTitle(_translate("MotorControl", "Motorcontroller"))
        self.step.setText(_translate("MotorControl", "motor step"))
        self.speed.setText(_translate("MotorControl", "motorspeed"))
self.seaence.setText(_translate("MotorControl", "spin sequance"))
        self.move.setText(_translate("MotorControl", "move"))
        self.reset.setText(_translate("MotorControl", "reset"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MotorControl = QtWidgets.QDialog()
    ui = Ui_MotorControl()
    ui.setupUi(MotorControl)
    MotorControl.show()
    sys.exit(app.exec_())
