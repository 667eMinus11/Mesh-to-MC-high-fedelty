import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from abstract_convertor import AbstractMeshConvertor


class MainWindow(QWidget):
    def __init__(self, convertor: AbstractMeshConvertor, parent=None):
        self.convertor: AbstractMeshConvertor = convertor

        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.browse_stl_button.clicked.connect(self.browse_stl)
        self.ui.browse_mesh_button.clicked.connect(self.browse_mesh)
        self.ui.convert_button.clicked.connect(self.convert)

    def browse_stl(self):
        file_path = QFileDialog.getOpenFileName(self, "Open STL file", filter="STL (*.stl)")[0]
        self.ui.stl_line_edit.setText(file_path)

    def browse_mesh(self):
        file_path = QFileDialog.getOpenFileName(self, "Open MESH file", filter="MESH (*.mesh)")[0]
        self.ui.mesh_line_edit.setText(file_path)

    def convert(self):
        self.convertor.convert(self.ui.stl_line_edit.text(), self.ui.voxelize_spin_box.value())
        output_file_path: str = QFileDialog.getSaveFileName(self, "Save schem file", filter="Schem (*.schem)")[0]
        if output_file_path != "":
            # Enforce the suffix schem
            output_file_path = output_file_path.removesuffix(".schem") + ".schem"
            self.convertor.save_to_file(output_file_path)
        # self.convertor.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    class fake_convertor(AbstractMeshConvertor):
        def convert(self, stl_file: str, voxelize: float):
            print(f"stl: {stl_file}")
            print(f"voxelize: {voxelize}")

        def show(self):
            print("Showing preview")

        def save_to_file(self, output_file: str):
            print(f'Saving to {output_file}')
    main_window = MainWindow(fake_convertor())
    main_window.show()
    sys.exit(app.exec())