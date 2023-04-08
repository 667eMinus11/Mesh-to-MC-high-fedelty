from abc import ABC, abstractmethod


class MeshConvertor(ABC):
    @abstractmethod
    def convert(self, stl_file: str, voxelize: float):
        ...