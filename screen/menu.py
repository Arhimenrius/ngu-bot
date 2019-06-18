from screen.clickable import Clickable


class Menu(Clickable):
    positions = {
        "BasicTraining": {"x": 230, "y": 45},
        "FightBoss": {"x": 230, "y": 75},
        "MoneyPit": {"x": 230, "y": 105},
        "Adventure": {"x": 230, "y": 135},
        "Inventory": {"x": 230, "y": 165},
        "Augmentation": {"x": 230, "y": 195},
        "AdvancedTraining": {"x": 230, "y": 225},
        "TimeMachine": {"x": 230, "y": 255},
        "BloodMagic": {"x": 230, "y": 285},
        "Wandoos": {"x": 230, "y": 315},
        "Ngu": {"x": 230, "y": 345},
        "Yggdrasil": {"x": 230, "y": 375},
        "GoldDiggers": {"x": 230, "y": 405},
        "BeardsOfPower": {"x": 230, "y": 435},
        "Rebirth": {"x": 80, "y": 420},
    }

    def basic_training(self):
        self.clickLeft(
            self.positions["BasicTraining"]["x"],
            self.positions["BasicTraining"]["y"]
        )

    def fight_boss(self):
        self.clickLeft(
            self.positions["FightBoss"]["x"],
            self.positions["FightBoss"]["y"]
        )

    def money_pit(self):
        self.clickLeft(
            self.positions["MoneyPit"]["x"],
            self.positions["MoneyPit"]["y"]
        )

    def adventure(self):
        self.clickLeft(
            self.positions["Adventure"]["x"],
            self.positions["Adventure"]["y"]
        )

    def inventory(self):
        self.clickLeft(
            self.positions["Inventory"]["x"],
            self.positions["Inventory"]["y"]
        )

    def augmentation(self):
        self.clickLeft(
            self.positions["Augmentation"]["x"],
            self.positions["Augmentation"]["y"]
        )

    def advanced_training(self):
        self.clickLeft(
            self.positions["AdvancedTraining"]["x"],
            self.positions["AdvancedTraining"]["y"]
        )

    def time_machine(self):
        self.clickLeft(
            self.positions["TimeMachine"]["x"],
            self.positions["TimeMachine"]["y"]
        )

    def blood_magic(self):
        self.clickLeft(
            self.positions["BloodMagic"]["x"],
            self.positions["BloodMagic"]["y"]
        )

    def wandoos(self):
        self.clickLeft(
            self.positions["Wandoos"]["x"],
            self.positions["Wandoos"]["y"]
        )

    def ngu(self):
        self.clickLeft(
            self.positions["Ngu"]["x"],
            self.positions["Ngu"]["y"]
        )

    def yggdrasil(self):
        self.clickLeft(
            self.positions["Yggdrasil"]["x"],
            self.positions["Yggdrasil"]["y"]
        )

    def gold_diggers(self):
        self.clickLeft(
            self.positions["GoldDiggers"]["x"],
            self.positions["GoldDiggers"]["y"]
        )

    def beards_of_power(self):
        self.clickLeft(
            self.positions["BeardsOfPower"]["x"],
            self.positions["BeardsOfPower"]["y"]
        )

    def rebirth(self):
        self.clickLeft(
            self.positions["Rebirth"]["x"],
            self.positions["Rebirth"]["y"]
        )
