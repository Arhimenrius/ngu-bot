from screen.clickable import Clickable


class TimeMachine(Clickable):
    positions = {
        "MachineSpeedAdd": {"x": 530, "y": 230},
        "MachineSpeedReduce": {"x": 565, "y": 230},
        "GoldMultiplierAdd": {"x": 530, "y": 330},
        "GoldMultiplierReduce": {"x": 565, "y": 330},
    }

    def machine_speed_add(self):
        self.clickLeft(
            self.positions["MachineSpeedAdd"]["x"],
            self.positions["MachineSpeedAdd"]["y"]
        )

    def machine_speed_reduce(self):
        self.clickLeft(
            self.positions["MachineSpeedReduce"]["x"],
            self.positions["MachineSpeedReduce"]["y"]
        )

    def gold_multiplier_add(self):
        self.clickLeft(
            self.positions["GoldMultiplierAdd"]["x"],
            self.positions["GoldMultiplierAdd"]["y"]
        )

    def gold_multiplier_reduce(self):
        self.clickLeft(
            self.positions["GoldMultiplierReduce"]["x"],
            self.positions["GoldMultiplierReduce"]["y"]
        )
