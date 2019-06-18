from screen.advanced_training import AdvancedTraining
from screen.adventure import Adventure
from screen.augmentation import Augmentation
from screen.basic_training import BasicTraining
from screen.beards_of_power import BeardsOfPower
from screen.blood_magic import BloodMagic
from screen.fight_boss import FightBoss
from screen.gold_diggers import GoldDiggers
from screen.inventory import Inventory
from screen.menu import Menu
from screen.money_pit import MoneyPit
from screen.ngu import Ngu
from screen.rebirth import Rebirth
from screen.time_machine import TimeMachine
from screen.wandoos import Wandoos
from screen.yggdrasil import Yggdrasil


class Screens:
    start_position_x = 0
    start_position_y = 0
    advancedTraining = None
    adventure = None
    augmentation = None
    basicTraining = None
    beardsOfPower = None
    bloodMagic = None
    fightBoss = None
    goldDiggers = None
    inventory = None
    menu = None
    moneyPit = None
    ngu = None
    rebirth = None
    timeMachine = None
    wandoos = None
    yggdrasil = None

    def __init__(self, start_position_x, start_position_y):
        self.start_position_x = start_position_x
        self.start_position_y = start_position_y
        self.advancedTraining = AdvancedTraining(self.start_position_x, self.start_position_y)
        self.adventure = Adventure(self.start_position_x, self.start_position_y)
        self.augmentation = Augmentation(self.start_position_x, self.start_position_y)
        self.basicTraining = BasicTraining(self.start_position_x, self.start_position_y)
        self.beardsOfPower = BeardsOfPower(self.start_position_x, self.start_position_y)
        self.bloodMagic = BloodMagic(self.start_position_x, self.start_position_y)
        self.fightBoss = FightBoss(self.start_position_x, self.start_position_y)
        self.goldDiggers = GoldDiggers(self.start_position_x, self.start_position_y)
        self.inventory = Inventory(self.start_position_x, self.start_position_y)
        self.menu = Menu(self.start_position_x, self.start_position_y)
        self.moneyPit = MoneyPit(self.start_position_x, self.start_position_y)
        self.ngu = Ngu(self.start_position_x, self.start_position_y)
        self.rebirth = Rebirth(self.start_position_x, self.start_position_y)
        self.timeMachine = TimeMachine(self.start_position_x, self.start_position_y)
        self.wandoos = Wandoos(self.start_position_x, self.start_position_y)
        self.yggdrasil = Yggdrasil(self.start_position_x, self.start_position_y)
