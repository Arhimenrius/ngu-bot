from screen.clickable import Clickable


class FightBoss(Clickable):
    positions = {
        "Nuke": {"x": 625, "y": 155},
        "Fight": {"x": 625, "y": 260},
    }

    def nuke(self):
        self.clickLeft(
            self.positions["Nuke"]["x"],
            self.positions["Nuke"]["y"]
        )

    def fight(self):
        self.clickLeft(
            self.positions["Fight"]["x"],
            self.positions["Fight"]["y"]
        )
