from screen.clickable import Clickable


class BloodMagic(Clickable):
    positions = {
        "GrandTheftBloodBankAdd": {"x": 495, "y": 365},
        "GrandTheftBloodBankReduce": {"x": 530, "y": 365},
    }

    def grand_theft_blood_bank_add(self):
        self.clickLeft(
            self.positions["GrandTheftBloodBankAdd"]["x"],
            self.positions["GrandTheftBloodBankAdd"]["y"]
        )

    def grand_theft_blood_bank_reduce(self):
        self.clickLeft(
            self.positions["GrandTheftBloodBankReduce"]["x"],
            self.positions["GrandTheftBloodBankReduce"]["y"]
        )
