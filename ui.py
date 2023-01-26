from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(992, 817)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("background-color:rgb(85, 85, 127);\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setStyleSheet("color:white;\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QLabel{\n"
"    color:rgb(255, 170, 255);\n"
"font: 20 8pt \"Aileron Heavy\";\n"
"padding:10px;\n"
"}")
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setStyleSheet("font: 36pt \"Sage\";\n"
"color:white;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.texte = QtWidgets.QLineEdit(self.tab)
        self.texte.setObjectName("texte")
        self.texte.setMinimumWidth(200)
        self.texte.setMinimumHeight(100)
        self.gridLayout_2.addWidget(self.texte, 1, 1, 1, 1)

        self.generate = QtWidgets.QPushButton(self.tab)
        self.generate.setObjectName("generate")
        self.generate.setMaximumWidth(100)
        self.generate.setMinimumWidth(100)
        self.generate.setMinimumHeight(50)
        self.generate.setStyleSheet("border-radius:45%;\n"
"border: 5px double rgb(255, 255, 255);\n"
"color:rgb(255, 255, 255);\n"
"font-size:10px;\n"
"")
        self.gridLayout_2.addWidget(self.generate, 1, 2, 1, 1)



        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_55 = QtWidgets.QLabel(self.tab)
        self.label_55.setObjectName("label_55")
        self.gridLayout_2.addWidget(self.label_55, 3, 1, 1, 1)


        
        self.label_55 = QtWidgets.QLabel(self.tab)
        self.label_55.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)



        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("QLabel{\n"
"    color:rgb(255, 170, 255);\n"
"font: 20 8pt \"Aileron Heavy\";\n"
"padding:10px;\n"
"}")
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setStyleSheet("font: 36pt \"Sage\";\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Steganographie-Vision"))
        Form.setWindowIcon(QtGui.QIcon('resources/logo.png'))
        self.label.setText(_translate("Form", "Cryptage du texte dans la photo"))
        self.label_4.setText(_translate("Form", "Etape 1 : Ecriture du texte"))
        self.label_7.setText(_translate("Form", "Etape 5 : Fusion des deux images pour cacher le texte"))
        self.label_3.setText(_translate("Form", "Etape 4 : Conversion de l\'image BGR en YCRCB sur 16bits"))
        self.label_5.setText(_translate("Form", "Etape 2 : Génération d\'une image de 8bits du texte"))
        self.label_6.setText(_translate("Form", "Etape 3 : Désignation d\'une image BGR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Cryptage"))
        self.label_2.setText(_translate("Form", "Decryptage et extraction du texte"))
        self.label_8.setText(_translate("Form", "Etape 1 : Désignation de l\'image avec un message caché"))
        self.label_9.setText(_translate("Form", "Etape 2: Création d\'une nouvelle image de 8bits"))
        self.label_10.setText(_translate("Form", "Extraction du texte de l\'image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Decryptage"))
        self.generate.setText(_translate("Form", "►"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
