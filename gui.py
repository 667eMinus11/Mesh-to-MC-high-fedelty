import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox

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

        self.ui.browse_obj_button.clicked.connect(self.browse_obj)
        self.ui.convert_button.clicked.connect(self.convert)

    def browse_obj(self):
        file_path = QFileDialog.getOpenFileName(self, "Open OBJ file", filter="All (*);;OBJ (*.obj)", selectedFilter="OBJ (*.obj)")[0]
        self.ui.obj_line_edit.setText(file_path)

    @property
    def obj_file(self) -> str:
        return self.ui.obj_line_edit.text()

    @property
    def voxel_size(self) -> str:
        return self.ui.voxel_size_spin_box.value()

    @property
    def use_high_res(self) -> bool:
        return self.ui.high_res_check_box.isChecked()

    def convert(self):
        try:
            if self.obj_file == "":
                raise Exception("Missing obj file")
            if self.voxel_size <= 0:
                raise ValueError("Voxel size must be a positive number.")
            if self.voxel_size < 0.01:
                preview = QMessageBox.warning(self, "Voxel size warning", f"You are using a voxel size below 0.01 ({self.voxel_size}). Are you sure you want to continue?", QMessageBox.Yes | QMessageBox.Abort, QMessageBox.Abort)
                if preview == QMessageBox.Abort:
                    return

            self.convertor.convert(self.obj_file, self.voxel_size, self.use_high_res)
        except Exception as e:
            QMessageBox.critical(self, "Error", f'Convertion failed with error: "{e}"', QMessageBox.Cancel)
            return

        preview = QMessageBox.question(self, "Preview file?", "Do you want to preview the object?", QMessageBox.Yes | QMessageBox.No)
        if preview == QMessageBox.Yes:
            try:
                self.convertor.show()
            except Exception as e:
                QMessageBox.critical(self, "Error", f'Preview failed with error: "{e}"', QMessageBox.Close)

        save = QMessageBox.question(self, "Safe to file?", "Do you want to save the schematics to a file?", QMessageBox.Save | QMessageBox.No)
        if save == QMessageBox.Save:
            output_file_path: str = QFileDialog.getSaveFileName(self, "Save schem file", filter="Schem (*.schem)")[0]
            # Enforce the suffix schem
            output_file_path = output_file_path.removesuffix(".schem") + ".schem"
            try:
                if output_file_path.removesuffix(".schem") == "":
                    raise Exception("Empty file name")
                self.convertor.save_to_file(output_file_path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f'Saving failed with error: "{e}"', QMessageBox.Close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    class fake_convertor(AbstractMeshConvertor):
        def __init__(self) -> None:
            super().__init__()
            self._converted_object = None

        def convert(self, obj_file: str, voxel_size: float, use_high_resolution: bool):
            print(f"obj: {obj_file}")
            print(f"voxel size: {voxel_size}")
            print(f"High res: {use_high_resolution}")
            self._converted_object = f'file{obj_file}@{voxel_size}'

        def show(self):
            assert(self._converted_object is not None)
            print(f"Showing preview for {self._converted_object}")

        def save_to_file(self, output_file: str):
            assert(self._converted_object is not None)
            print(f'Saving {self._converted_object} to {output_file}')
    main_window = MainWindow(fake_convertor())
    main_window.show()
    sys.exit(app.exec())