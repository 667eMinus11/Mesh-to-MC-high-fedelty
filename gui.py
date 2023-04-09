import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QErrorMessage

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

    @property
    def stl_file(self) -> str:
        return self.ui.stl_line_edit.text()

    @property
    def mesh_file(self) -> str:
        return self.ui.mesh_line_edit.text()

    @property
    def voxelize_value(self) -> str:
        return self.ui.voxelize_spin_box.value()

    def convert(self):
        try:
            if self.stl_file == "":
                raise Exception("Missing stl file")
            self.convertor.convert(self.stl_file, self.voxelize_value)
        except Exception as e:
            QErrorMessage(self).showMessage(f'Convertion failed with error: "{e}"')
            return

        preview = QMessageBox.question(self, "Preview file?", "Do you want to preview the object?", QMessageBox.Yes | QMessageBox.No)
        if preview == QMessageBox.Yes:
            try:
                self.convertor.show()
            except Exception as e:
                QErrorMessage(self).showMessage(f'Preview failed with error: "{e}"')


        save = QMessageBox.question(self, "Safe to file?", "Do you want to save the schematics to a file?", QMessageBox.Yes | QMessageBox.No)
        if save == QMessageBox.Yes:
            output_file_path: str = QFileDialog.getSaveFileName(self, "Save schem file", filter="Schem (*.schem)")[0]
            # Enforce the suffix schem
            output_file_path = output_file_path.removesuffix(".schem") + ".schem"
            try:
                if output_file_path.removesuffix(".schem") == "":
                    raise Exception("Empty file name")
                self.convertor.save_to_file(output_file_path)
            except Exception as e:
                QErrorMessage(self).showMessage(f'Saving failed with error: "{e}"')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    class fake_convertor(AbstractMeshConvertor):
        def __init__(self) -> None:
            super().__init__()
            self._converted_object = None

        def convert(self, stl_file: str, voxelize: float):
            print(f"stl: {stl_file}")
            print(f"voxelize: {voxelize}")
            self._converted_object = f'file{stl_file}@{voxelize}'

        def show(self):
            assert(self._converted_object is not None)
            print(f"Showing preview for {self._converted_object}")

        def save_to_file(self, output_file: str):
            assert(self._converted_object is not None)
            print(f'Saving {self._converted_object} to {output_file}')
    main_window = MainWindow(fake_convertor())
    main_window.show()
    sys.exit(app.exec())