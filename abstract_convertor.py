from abc import ABC, abstractmethod


class AbstractMeshConvertor(ABC):
    @abstractmethod
    def convert(self, stl_file: str, voxelize: float):
        ...