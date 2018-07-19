# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MotorControl(object):
    def setupUi(self, MotorControl):
        MotorControl.setObjectName("MotorControl")
        MotorControl.resize(487, 331)
        
        self.stepcontroler = QtWidgets.QSpinBox(MotorControl)
        self.stepcontroler.setGeometry(QtCore.QRect(130, 20, 101, 31))
        self.stepcontroler.setMinimum(-999)
        self.stepcontroler.setMaximum(999)
        self.stepcontroler.setObjectName("stepcontroler")
        
        self.progressBar = QtWidgets.QProgressBar(MotorControl)
        self.progressBar.setGeometry(QtCore.QRect(50, 260, 161, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        
        self.speedcontrol = QtWidgets.QSlider(MotorControl)
        self.speedcontrol.setGeometry(QtCore.QRect(130, 70, 311, 22))
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
        
        self.reset = QtWidgets.QPushButton(MotorControl)
        self.reset.setGeometry(QtCore.QRect(240, 260, 92, 36))
        self.reset.setObjectName("reset")



        self.retranslateUi(MotorControl)
        self.speedcontrol.valueChanged['int'].connect(MotorControl.exec)
        
        self.sequenceselector.sliderReleased.connect(MotorControl.exec)
        
        self.stepcontroler.valueChanged['int'].connect(MotorControl.exec)
        
        self.stepcontroler.valueChanged['QString'].connect(self.lengthUnit.setText)
        
        self.reset.clicked.connect(MotorControl.reset)
        
        self.move.clicked['bool'].connect(MotorControl.open)
        
        self.move.clicked.connect(self.progressBar.update)
        
        QtCore.QMetaObject.connectSlotsByName(MotorControl)

    def retranslateUi(self, MotorControl):
        _translate = QtCore.QCoreApplication.translate
        MotorControl.setWindowTitle(_translate("MotorControl", "Dialog"))
        self.step.setText(_translate("MotorControl", "motor step"))
        self.speed.setText(_translate("MotorControl", "motorspeed"))
        self.lengthUnit.setText(_translate("MotorControl", "<html><head/><body><p><span style=\" font-size:14pt;\">㎛</span></p></body></html>"))
        self.seaence.setText(_translate("MotorControl", "spin sequance"))
        self.move.setText(_translate("MotorControl", "move"))
        self.reset.setText(_translate("MotorControl", "reset"))
