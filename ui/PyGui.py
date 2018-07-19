# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(654, 295)
        self.ok_cancel = QtWidgets.QDialogButtonBox(Dialog)
        self.ok_cancel.setGeometry(QtCore.QRect(100, 260, 301, 32))
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")
        self.stepcontroler = QtWidgets.QSpinBox(Dialog)
        self.stepcontroler.setGeometry(QtCore.QRect(130, 20, 101, 31))
        self.stepcontroler.setMinimum(-999)
        self.stepcontroler.setMaximum(999)
        self.stepcontroler.setObjectName("stepcontroler")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(50, 260, 161, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(260, 20, 181, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.speedcontrol = QtWidgets.QSlider(Dialog)
        self.speedcontrol.setGeometry(QtCore.QRect(130, 70, 311, 22))
        self.speedcontrol.setOrientation(QtCore.Qt.Horizontal)
        self.speedcontrol.setObjectName("speedcontrol")
        self.step = QtWidgets.QLabel(Dialog)
        self.step.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.step.setObjectName("step")
        self.speed = QtWidgets.QLabel(Dialog)
        self.speed.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.speed.setObjectName("speed")
        self.length = QtWidgets.QLabel(Dialog)
        self.length.setGeometry(QtCore.QRect(450, 20, 31, 31))
        self.length.setObjectName("length")
        self.seaence = QtWidgets.QLabel(Dialog)
        self.seaence.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.seaence.setObjectName("seaence")
        self.sequenceselector = QtWidgets.QSlider(Dialog)
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

        self.retranslateUi(Dialog)
        self.ok_cancel.accepted.connect(Dialog.accept)
        self.ok_cancel.rejected.connect(Dialog.reject)
        self.stepcontroler.valueChanged['QString'].connect(self.textBrowser.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.step.setText(_translate("Dialog", "motor step"))
        self.speed.setText(_translate("Dialog", "motorspeed"))
        self.length.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">㎛</span></p></body></html>"))
        self.seaence.setText(_translate("Dialog", "spin sequance"))

