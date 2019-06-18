from screen.clickable import Clickable


class Augmentation(Clickable):
    positions = {
        "EnergyBusterAdd": {"x": 535, "y": 520},
        "EnergyBusterReduce": {"x": 570, "y": 520},
        "ChargeShotAdd": {"x": 535, "y": 550},
        "ChargeShotReduce": {"x": 570, "y": 550},
    }

    def energy_buster_add(self):
        self.clickLeft(
            self.positions["EnergyBusterAdd"]["x"],
            self.positions["EnergyBusterAdd"]["y"]
        )

    def energy_buster_reduce(self):
        self.clickLeft(
            self.positions["EnergyBusterReduce"]["x"],
            self.positions["EnergyBusterReduce"]["y"]
        )

    def charge_shot_add(self):
        self.clickLeft(
            self.positions["ChargeShotAdd"]["x"],
            self.positions["ChargeShotAdd"]["y"]
        )

    def charge_shot_reduce(self):
        self.clickLeft(
            self.positions["ChargeShotReduce"]["x"],
            self.positions["ChargeShotReduce"]["y"]
        )
