# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created: Mon Dec 26 00:20:07 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ExportFileDialog(object):
    def setupUi(self, ExportFileDialog):
        ExportFileDialog.setObjectName("ExportFileDialog")
        ExportFileDialog.resize(624, 279)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExportFileDialog.sizePolicy().hasHeightForWidth())
        ExportFileDialog.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QtGui.QGridLayout(ExportFileDialog)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBoxSource = QtGui.QComboBox(ExportFileDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSource.sizePolicy().hasHeightForWidth())
        self.comboBoxSource.setSizePolicy(sizePolicy)
        self.comboBoxSource.setObjectName("comboBoxSource")
        self.gridLayout_4.addWidget(self.comboBoxSource, 0, 1, 1, 1)
        self.btnBrowseSource = QtGui.QPushButton(ExportFileDialog)
        self.btnBrowseSource.setObjectName("btnBrowseSource")
        self.gridLayout_4.addWidget(self.btnBrowseSource, 0, 2, 1, 1)
        self.labelSource = QtGui.QLabel(ExportFileDialog)
        self.labelSource.setObjectName("labelSource")
        self.gridLayout_4.addWidget(self.labelSource, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelEncoding = QtGui.QLabel(ExportFileDialog)
        self.labelEncoding.setObjectName("labelEncoding")
        self.gridLayout_6.addWidget(self.labelEncoding, 0, 0, 1, 1)
        self.comboBoxEncoding = QtGui.QComboBox(ExportFileDialog)
        self.comboBoxEncoding.setObjectName("comboBoxEncoding")
        self.gridLayout_6.addWidget(self.comboBoxEncoding, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 6, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelDestination = QtGui.QLabel(ExportFileDialog)
        self.labelDestination.setObjectName("labelDestination")
        self.gridLayout_5.addWidget(self.labelDestination, 0, 0, 1, 1)
        self.btnBrowseDestination = QtGui.QPushButton(ExportFileDialog)
        self.btnBrowseDestination.setObjectName("btnBrowseDestination")
        self.gridLayout_5.addWidget(self.btnBrowseDestination, 0, 3, 1, 1)
        self.lineEditDestination = QtGui.QLineEdit(ExportFileDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDestination.sizePolicy().hasHeightForWidth())
        self.lineEditDestination.setSizePolicy(sizePolicy)
        self.lineEditDestination.setObjectName("lineEditDestination")
        self.gridLayout_5.addWidget(self.lineEditDestination, 0, 1, 1, 1)
        self.btnOverwrite = QtGui.QPushButton(ExportFileDialog)
        self.btnOverwrite.setObjectName("btnOverwrite")
        self.gridLayout_5.addWidget(self.btnOverwrite, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditOtherSeparator = QtGui.QLineEdit(ExportFileDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditOtherSeparator.sizePolicy().hasHeightForWidth())
        self.lineEditOtherSeparator.setSizePolicy(sizePolicy)
        self.lineEditOtherSeparator.setObjectName("lineEditOtherSeparator")
        self.gridLayout_3.addWidget(self.lineEditOtherSeparator, 2, 1, 1, 1)
        self.radioBtnOtherSeparator = QtGui.QRadioButton(ExportFileDialog)
        self.radioBtnOtherSeparator.setObjectName("radioBtnOtherSeparator")
        self.gridLayout_3.addWidget(self.radioBtnOtherSeparator, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        self.comboBoxSeparator = QtGui.QComboBox(ExportFileDialog)
        self.comboBoxSeparator.setObjectName("comboBoxSeparator")
        self.gridLayout_2.addWidget(self.comboBoxSeparator, 0, 1, 1, 1)
        self.labelSeparator = QtGui.QLabel(ExportFileDialog)
        self.labelSeparator.setObjectName("labelSeparator")
        self.gridLayout_2.addWidget(self.labelSeparator, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ExportFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(ExportFileDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ExportFileDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ExportFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportFileDialog)

    def retranslateUi(self, ExportFileDialog):
        ExportFileDialog.setWindowTitle(QtGui.QApplication.translate("ExportFileDialog", "Export File", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowseSource.setText(QtGui.QApplication.translate("ExportFileDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSource.setText(QtGui.QApplication.translate("ExportFileDialog", "Source Path", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEncoding.setText(QtGui.QApplication.translate("ExportFileDialog", "Encoding:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDestination.setText(QtGui.QApplication.translate("ExportFileDialog", "Destination Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowseDestination.setText(QtGui.QApplication.translate("ExportFileDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOverwrite.setText(QtGui.QApplication.translate("ExportFileDialog", "Overwrite", None, QtGui.QApplication.UnicodeUTF8))
        self.radioBtnOtherSeparator.setText(QtGui.QApplication.translate("ExportFileDialog", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSeparator.setText(QtGui.QApplication.translate("ExportFileDialog", "Separator:", None, QtGui.QApplication.UnicodeUTF8))

