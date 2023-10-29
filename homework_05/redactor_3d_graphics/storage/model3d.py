from files3d import Files3D
from renders import Renders
from animation import Animation


class Model3D:
    def __init__(self, file_name: str, files3d: Files3D, renders: Renders, animation: Animation):
        self.file_name = file_name
        self.files3d = files3d
        self.renders = renders
        self.animation = animation
