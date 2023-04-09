from abc import ABC, abstractmethod


class AbstractMeshConvertor(ABC):
    @abstractmethod
    def convert(self, stl_file: str, voxelize: float):
        ...

    @abstractmethod
    def show(self):
        ...

    @abstractmethod
    def save_to_file(self, output_file: str):
        ...