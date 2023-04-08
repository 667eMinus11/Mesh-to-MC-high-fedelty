import sys
from typing import Type

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from convertor import MeshConvertor


class MainWindow(QWidget):
    def __init__(self, convertor: Type[MeshConvertor], parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.browse_stl_button.clicked.connect(self.browse_stl)
        self.ui.browse_mesh_button.clicked.connect(self.browse_mesh)

    def browse_stl(self):
        file_path = QFileDialog.getOpenFileName(self, "Open STL file", filter="STL (*.stl)")[0]
        self.ui.stl_line_edit.setText(file_path)

    def browse_mesh(self):
        file_path = QFileDialog.getOpenFileName(self, "Open MESH file", filter="MESH (*.mesh)")[0]
        self.ui.mesh_line_edit.setText(file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    class fake_convertor(MeshConvertor):
        def convert(self):
            return super().convert()
    main_window = MainWindow(fake_convertor)
    main_window.show()
    sys.exit(app.exec())