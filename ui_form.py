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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.mesh_line_edit = QLineEdit(Widget)
        self.mesh_line_edit.setObjectName(u"mesh_line_edit")

        self.horizontalLayout_3.addWidget(self.mesh_line_edit)

        self.browse_mesh_button = QPushButton(Widget)
        self.browse_mesh_button.setObjectName(u"browse_mesh_button")

        self.horizontalLayout_3.addWidget(self.browse_mesh_button)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

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
        self.stl_label = QLabel(Widget)
        self.stl_label.setObjectName(u"stl_label")

        self.horizontalLayout.addWidget(self.stl_label)

        self.stl_line_edit = QLineEdit(Widget)
        self.stl_line_edit.setObjectName(u"stl_line_edit")

        self.horizontalLayout.addWidget(self.stl_line_edit)

        self.browse_stl_button = QPushButton(Widget)
        self.browse_stl_button.setObjectName(u"browse_stl_button")

        self.horizontalLayout.addWidget(self.browse_stl_button)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.voxelize_spin_box = QDoubleSpinBox(Widget)
        self.voxelize_spin_box.setObjectName(u"voxelize_spin_box")
        self.voxelize_spin_box.setMaximum(1.000000000000000)
        self.voxelize_spin_box.setValue(0.050000000000000)

        self.horizontalLayout_2.addWidget(self.voxelize_spin_box)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"MESH file:", None))
        self.browse_mesh_button.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.convert_button.setText(QCoreApplication.translate("Widget", u"Generate", None))
        self.stl_label.setText(QCoreApplication.translate("Widget", u"STL file:", None))
        self.browse_stl_button.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Resolution??", None))
    # retranslateUi

