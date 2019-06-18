from screen.clickable import Clickable


class AdvancedTraining(Clickable):
    positions = {
        "AdventureToughnessPlusAdd": {"x": 0, "y": 0},
        "AdventureToughnessPlusReduce": {"x": 0, "y": 0},
        "AdventurePowerPlusAdd": {"x": 0, "y": 0},
        "AdventurePowerPlusReduce": {"x": 0, "y": 0},
        "BlockDamageReductionAdd": {"x": 0, "y": 0},
        "BlockDamageReductionReduce": {"x": 0, "y": 0},
        "WandoosEnergyDumpPlusAdd": {"x": 0, "y": 0},
        "WandoosEnergyDumpPlusReduce": {"x": 0, "y": 0},
        "WandoosMagicDumpPlusAdd": {"x": 0, "y": 0},
        "WandoosMagicDumpPlusReduce": {"x": 0, "y": 0},
    }

    def adventure_toughness_plus_add(self):
        self.clickLeft(
            self.positions["AdventureToughnessPlusAdd"]["x"],
            self.positions["AdventureToughnessPlusAdd"]["y"]
        )

    def adventure_toughness_plus_reduce(self):
        self.clickLeft(
            self.positions["AdventureToughnessPlusReduce"]["x"],
            self.positions["AdventureToughnessPlusReduce"]["y"]
        )

    def adventure_power_plus_add(self):
        self.clickLeft(
            self.positions["AdventurePowerPlusAdd"]["x"],
            self.positions["AdventurePowerPlusAdd"]["y"]
        )

    def adventure_power_plus_reduce(self):
        self.clickLeft(
            self.positions["AdventurePowerPlusReduce"]["x"],
            self.positions["AdventurePowerPlusReduce"]["y"]
        )

    def block_damage_reduction_add(self):
        self.clickLeft(
            self.positions["BlockDamageReductionAdd"]["x"],
            self.positions["BlockDamageReductionAdd"]["y"]
        )

    def block_damage_reduction_reduce(self):
        self.clickLeft(
            self.positions["BlockDamageReductionReduce"]["x"],
            self.positions["BlockDamageReductionReduce"]["y"]
        )

    def wandoos_energy_dump_plus_add(self):
        self.clickLeft(
            self.positions["WandoosEnergyDumpPlusAdd"]["x"],
            self.positions["WandoosEnergyDumpPlusAdd"]["y"]
        )

    def wandoos_energy_dump_plus_reduce(self):
        self.clickLeft(
            self.positions["WandoosEnergyDumpPlusReduce"]["x"],
            self.positions["WandoosEnergyDumpPlusReduce"]["y"]
        )

    def wandoos_magic_dump_plus_add(self):
        self.clickLeft(
            self.positions["WandoosMagicDumpPlusAdd"]["x"],
            self.positions["WandoosMagicDumpPlusAdd"]["y"]
        )

    def wandoos_magic_dump_plus_reduce(self):
        self.clickLeft(
            self.positions["WandoosMagicDumpPlusReduce"]["x"],
            self.positions["WandoosMagicDumpPlusReduce"]["y"]
        )
