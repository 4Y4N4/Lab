# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pic.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MotorControl(object):
    def setupUi(self, MotorControl):
        MotorControl.setObjectName("MotorControl")
        MotorControl.resize(487, 331)
        self.stepcontroller = QtWidgets.QSpinBox(MotorControl)
        self.stepcontroller.setGeometry(QtCore.QRect(130, 20, 101, 31))
        self.stepcontroller.setMinimum(-999)
        self.stepcontroller.setMaximum(999)
        self.stepcontroller.setObjectName("stepcontroller")
        self.progressBar = QtWidgets.QProgressBar(MotorControl)
        self.progressBar.setGeometry(QtCore.QRect(50, 260, 161, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.speedcontrol = QtWidgets.QSlider(MotorControl)
        self.speedcontrol.setGeometry(QtCore.QRect(130, 70, 311, 22))
        self.speedcontrol.setMinimum(-200)
        self.speedcontrol.setMaximum(200)
        self.speedcontrol.setOrientation(QtCore.Qt.Horizontal)
        self.speedcontrol.setObjectName("speedcontrol")
        self.step = QtWidgets.QLabel(MotorControl)
        self.step.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.step.setObjectName("step")
        self.speed = QtWidgets.QLabel(MotorControl)
        self.speed.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.speed.setObjectName("speed")
        self.lengthUnit = QtWidgets.QLabel(MotorControl)
        self.lengthUnit.setGeometry(QtCore.QRect(240, 20, 201, 31))
        self.lengthUnit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lengthUnit.setAutoFillBackground(True)
        self.lengthUnit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lengthUnit.setWordWrap(False)
        self.lengthUnit.setOpenExternalLinks(False)
        self.lengthUnit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lengthUnit.setObjectName("lengthUnit")
        self.seaence = QtWidgets.QLabel(MotorControl)
        self.seaence.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.seaence.setObjectName("seaence")
        self.sequenceselector = QtWidgets.QSlider(MotorControl)
        self.sequenceselector.setGeometry(QtCore.QRect(130, 160, 311, 22))
        self.sequenceselector.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sequenceselector.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.sequenceselector.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sequenceselector.setMaximum(2)
        self.sequenceselector.setSingleStep(1)
        self.sequenceselector.setPageStep(1)
        self.sequenceselector.setOrientation(QtCore.Qt.Horizontal)
        self.sequenceselector.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sequenceselector.setTickInterval(1)
        self.sequenceselector.setObjectName("sequenceselector")
        self.move = QtWidgets.QPushButton(MotorControl)
        self.move.setGeometry(QtCore.QRect(370, 260, 92, 36))
        self.move.setObjectName("move")
        self.speedBar = QtWidgets.QLabel(MotorControl)
        self.speedBar.setGeometry(QtCore.QRect(130, 100, 181, 20))
        self.speedBar.setObjectName("speedBar")

        self.retranslateUi(MotorControl)
        QtCore.QMetaObject.connectSlotsByName(MotorControl)

    def retranslateUi(self, MotorControl):
        _translate = QtCore.QCoreApplication.translate
        MotorControl.setWindowTitle(_translate("MotorControl", "Dialog"))
        self.step.setText(_translate("MotorControl", "motor step"))
        self.speed.setText(_translate("MotorControl", "motorspeed"))
        self.lengthUnit.setText(_translate("MotorControl", "<html><head/><body><p><span style=\" font-size:14pt;\">㎛</span></p></body></html>"))
        self.seaence.setText(_translate("MotorControl", "spin sequance"))
        self.move.setText(_translate("MotorControl", "move"))
        self.speedBar.setText(_translate("MotorControl", "㎛"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MotorControl = QtWidgets.QDialog()
    ui = Ui_MotorControl()
    ui.setupUi(MotorControl)
    MotorControl.show()
    sys.exit(app.exec_())

