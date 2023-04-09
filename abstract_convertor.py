from abc import ABC, abstractmethod


class AbstractMeshConvertor(ABC):
    @abstractmethod
    def convert(self, stl_file: str, voxel_size: float, use_high_resolution: bool):
        ...

    @abstractmethod
    def show(self):
        ...

    @abstractmethod
    def save_to_file(self, output_file: str):
        ...