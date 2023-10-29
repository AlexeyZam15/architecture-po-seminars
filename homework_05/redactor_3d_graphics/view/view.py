from create_panel import CreatePanel
from load_panel import LoadPanel
from save_panel import SavePanel
from view_panel import ViewPanel
from view_inferface import ViewInterface


class View(ViewInterface):
    def __init__(self, load_panel: LoadPanel, save_panel: SavePanel, view_panel: ViewPanel):
        self.load_panel = load_panel
        self.save_panel = save_panel
        self.view_panel = view_panel

    def load_model3d(self) -> str:
        pass

    def save_model3d(self):
        pass

    def view_model3d(self):
        pass
