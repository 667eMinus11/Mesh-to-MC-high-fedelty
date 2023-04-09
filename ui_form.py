# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(500, 400)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.convert_button = QPushButton(Widget)
        self.convert_button.setObjectName(u"convert_button")

        self.horizontalLayout_4.addWidget(self.convert_button)


        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.obj_label = QLabel(Widget)
        self.obj_label.setObjectName(u"obj_label")

        self.horizontalLayout.addWidget(self.obj_label)

        self.obj_line_edit = QLineEdit(Widget)
        self.obj_line_edit.setObjectName(u"obj_line_edit")

        self.horizontalLayout.addWidget(self.obj_line_edit)

        self.browse_obj_button = QPushButton(Widget)
        self.browse_obj_button.setObjectName(u"browse_obj_button")

        self.horizontalLayout.addWidget(self.browse_obj_button)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.voxel_size_spin_box = QDoubleSpinBox(Widget)
        self.voxel_size_spin_box.setObjectName(u"voxel_size_spin_box")
        self.voxel_size_spin_box.setDecimals(3)
        self.voxel_size_spin_box.setMinimum(0.001000000000000)
        self.voxel_size_spin_box.setMaximum(100.000000000000000)
        self.voxel_size_spin_box.setSingleStep(0.500000000000000)
        self.voxel_size_spin_box.setValue(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.voxel_size_spin_box)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.high_res_check_box = QCheckBox(Widget)
        self.high_res_check_box.setObjectName(u"high_res_check_box")
        self.high_res_check_box.setChecked(True)

        self.horizontalLayout_3.addWidget(self.high_res_check_box)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.convert_button.setText(QCoreApplication.translate("Widget", u"Generate", None))
        self.obj_label.setText(QCoreApplication.translate("Widget", u"Obj file:", None))
        self.browse_obj_button.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Voxel Size", None))
        self.high_res_check_box.setText(QCoreApplication.translate("Widget", u"High Resolution", None))
    # retranslateUi

