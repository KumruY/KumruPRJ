from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self,Form):
        Form.setObjectName("Form")
        Form.resize(525,386)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("HorizantelLayout")
        self.verticalLayout=QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("VerticalLayout")
        self.image_label=QtWidgets.QLabel(Form)
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        self.control_button=QtWidgets.QPushButton(Form)
        self.control_button.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_button)
        self.horizontalLayout.addWidget(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self,Form):
        _translate=QtCore.QCoreApplication("Form","Cam view")
        self.image_label.setText(_translate("Form","TextLabel"))
        self.control_button.setText(_translate("Form","Start"))