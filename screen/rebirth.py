from screen.clickable import Clickable


class Rebirth(Clickable):
    positions = {
        "Rebirth": {"x": 550, "y": 520},
        "AcceptRebirth": {"x": 430, "y": 315},
    }

    def rebirth(self):
        self.clickLeft(
            self.positions["Rebirth"]["x"],
            self.positions["Rebirth"]["y"]
        )

    def accept_rebirth(self):
        self.clickLeft(
            self.positions["AcceptRebirth"]["x"],
            self.positions["AcceptRebirth"]["y"]
        )
