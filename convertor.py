from abc import ABC, abstractmethod


class MeshConvertor(ABC):
    def __init__(self, stl_file: str, voxelize: float):
        self.stl_file = stl_file
        self.voxelize = voxelize

    @abstractmethod
    def convert(self):
        ...