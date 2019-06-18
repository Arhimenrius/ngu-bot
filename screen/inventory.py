from screen.clickable import Clickable


class Inventory(Clickable):
    positions = {
        "InfinityBox": {"x": 625, "y": 115},
        "Loadout1": {"x": 330, "y": 255},
        "Loadout2": {"x": 360, "y": 255},
    }

    def infinity_box(self):
        self.clickRight(
            self.positions["InfinityBox"]["x"],
            self.positions["InfinityBox"]["y"]
        )

    def loadout1(self):
        self.clickLeft(
            self.positions["Loadout1"]["x"],
            self.positions["Loadout1"]["y"]
        )

    def loadout2(self):
        self.clickLeft(
            self.positions["Loadout2"]["x"],
            self.positions["Loadout2"]["y"]
        )
