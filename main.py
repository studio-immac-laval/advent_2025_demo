import pyxel
from day   import Day
from day01 import Day01
from day02 import Day02
from day03 import Day03
from day04 import Day04
from day05 import Day05
from day06 import Day06
from day07 import Day07
from day08 import Day08
from day09 import Day09
from day10 import Day10
from day11 import Day11
from day12 import Day12
from day13 import Day13
from day14 import Day14
from day15 import Day15
from day16 import Day16
from day17 import Day17
from day18 import Day18
from day19 import Day19
from day20 import Day20
from day21 import Day21
from day22 import Day22
from day23 import Day23
from day24 import Day24
from day25 import Day25

class App:
    def __init__(self) :
        pyxel.init(128, 128)
        pyxel.mouse(True)
        pyxel.load("advent.pyxres")
        self.days = [
            Day01(10, 10, 1, 1),
            Day02(33, 10, 2, 2),
            Day03(56, 10, 3, 3),
            Day04(79, 10, 4, 4),
            Day05(102, 10, 5, 5),
            Day06(10, 33, 6, 6),
            Day07(33, 33, 7, 8),
            Day08(56, 33, 8, 9),
            Day09(79, 33, 9, 10),
            Day10(102, 33, 10, 11),
            Day11(10, 56, 11, 12),
            Day12(33, 56, 12, 13),
            Day13(56, 56, 13, 14),
            Day14(79, 56, 14, 15),
            Day15(102, 56, 15, 1),
            Day16(10, 79, 16, 2),
            Day17(33, 79, 17, 3),
            Day18(56, 79, 18, 4),
            Day19(79, 79, 19, 5),
            Day20(102, 79, 20, 6),
            Day21(10, 102, 21, 8),
            Day22(33, 102, 22, 9),
            Day23(56, 102, 23, 10),
            Day24(79, 102, 24, 11),
            Day25(102, 102, 25, 8),
        ]
        self.openedDay = -1
        pyxel.run(self.update, self.draw)

    def update(self) :
        if self.openedDay == -1 :
            for i in range(len(self.days)) :
                self.days[i].update()
                if self.days[i].state == Day.STATE_OPENING :
                    self.openedDay = i
                    break
        else :
            self.days[self.openedDay].update()
            if self.days[self.openedDay].state == Day.STATE_CLOSED :
                self.openedDay = -1
    
    def draw(self) :
        pyxel.cls(7)

        # Aucun jour ouvert
        if self.openedDay == -1 :
            for i in range(len(self.days)) :
                self.days[i].draw()

        # Un jour en cours d'ouverture
        elif self.days[self.openedDay].state == Day.STATE_OPENING :
            for i in range(len(self.days)) :
                if i != self.openedDay :
                    self.days[i].draw()
            self.days[self.openedDay].draw()

        # Un jour ouvert
        else :
            self.days[self.openedDay].draw()

App()