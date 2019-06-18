from screen.clickable import Clickable


class Adventure(Clickable):
    positions = {
        "NextArea": {"x": 925, "y": 225},
    }

    def next_area(self):
        self.clickLeft(
            self.positions["NextArea"]["x"],
            self.positions["NextArea"]["y"]
        )
