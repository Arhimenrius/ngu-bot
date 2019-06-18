from screens import Screens
from time import sleep
import itertools


class Fast15:
    long_break = 1
    longer_break = 5
    screens = None
    areas_to_skip = 13
    repeat_amount_for_time_machine_first = 300
    repeat_amount_for_time_machine_second = 500
    infinity_box_usage_times = 6
    wait_for_orange_augment = 40
    time_for_quick_progress = 120
    time_for_wandoos = 120
    fight_clicks_on_the_end = 50

    def __init__(self, screens: Screens):
        self.screens = screens
        while True:
            self.new_rebirth()
            sleep(self.long_break)
            self.get_gold()
            sleep(self.long_break)
            self.more_gold()
            sleep(self.long_break)
            self.quick_progress()
            sleep(self.long_break)
            self.finishing_progress()
            sleep(self.long_break)
            self.last_kills()
            sleep(self.longer_break)

    def new_rebirth(self):
        self.screens.menu.rebirth()
        self.screens.rebirth.rebirth()
        self.screens.rebirth.accept_rebirth()

    def get_gold(self):
        self.screens.menu.fight_boss()
        self.screens.fightBoss.nuke()
        sleep(self.longer_break)
        self.screens.menu.adventure()
        for _ in itertools.repeat(None, self.areas_to_skip):
            self.screens.adventure.next_area()
        self.screens.menu.inventory()
        self.screens.inventory.loadout1()
        for _ in itertools.repeat(None, self.infinity_box_usage_times):
            self.screens.inventory.infinity_box()
        return

    def more_gold(self):
        counter = 0
        self.screens.menu.time_machine()

        while True:
            self.screens.timeMachine.machine_speed_add()
            self.screens.timeMachine.gold_multiplier_add()
            counter = counter + 1
            print(counter)
            if counter == self.repeat_amount_for_time_machine_first:
                break

        self.screens.menu.inventory()
        self.screens.inventory.loadout2()

        self.screens.menu.time_machine()
        counter = 0

        while True:
            self.screens.timeMachine.machine_speed_add()
            self.screens.timeMachine.gold_multiplier_add()
            counter = counter + 1
            print(counter)
            if counter == self.repeat_amount_for_time_machine_second:
                break

        self.screens.timeMachine.machine_speed_reduce()
        self.screens.timeMachine.gold_multiplier_reduce()

    def quick_progress(self):
        self.screens.menu.blood_magic()
        self.screens.bloodMagic.grand_theft_blood_bank_add()

        self.screens.menu.augmentation()
        self.screens.augmentation.charge_shot_add()
        sleep(self.wait_for_orange_augment)
        self.screens.augmentation.charge_shot_reduce()
        self.screens.augmentation.energy_buster_add()
        sleep(self.time_for_quick_progress)

        self.screens.augmentation.energy_buster_reduce()
        self.screens.menu.blood_magic()
        self.screens.bloodMagic.grand_theft_blood_bank_reduce()
        return

    def finishing_progress(self):
        self.screens.menu.wandoos()
        self.screens.wandoos.energy_dump_add()
        self.screens.wandoos.magic_dump_add()
        sleep(self.time_for_wandoos)
        return

    def last_kills(self):
        self.screens.menu.fight_boss()
        for _ in itertools.repeat(None, self.fight_clicks_on_the_end):
            self.screens.fightBoss.fight()
        return
