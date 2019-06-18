from screen.clickable import Clickable


class Wandoos(Clickable):
    positions = {
        "EnergyDumpAdd": {"x": 555, "y": 250},
        "EnergyDumpReduce": {"x": 585, "y": 250},
        "MagicDumpAdd": {"x": 555, "y": 350},
        "MagicDumpReduce": {"x": 585, "y": 350},
    }

    def energy_dump_add(self):
        self.clickLeft(
            self.positions["EnergyDumpAdd"]["x"],
            self.positions["EnergyDumpAdd"]["y"]
        )

    def energy_dump_reduce(self):
        self.clickLeft(
            self.positions["EnergyDumpReduce"]["x"],
            self.positions["EnergyDumpReduce"]["y"]
        )

    def magic_dump_add(self):
        self.clickLeft(
            self.positions["MagicDumpAdd"]["x"],
            self.positions["MagicDumpAdd"]["y"]
        )

    def magic_dump_reduce(self):
        self.clickLeft(
            self.positions["MagicDumpReduce"]["x"],
            self.positions["MagicDumpReduce"]["y"]
        )
