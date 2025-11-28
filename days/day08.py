import pyxel
from math import sqrt
from random import randint
from day import Day

class Day08(Day) :
    
    def __init__(self, x : int, y : int, number : int, color : int, author : str = "") :
        super().__init__(x, y, number, color, "Mathieu")
        self.santaX = 0
        self.santaY = 0
        self.coucouX = 0
        self.coucouY = 0

    def update(self):
        super().update()
        if  self.state == Day.STATE_OPENING :
            self.santaX = randint(10, 90)
            self.santaY = randint(20, 90)
            self.coucouX = (self.santaX + 12) if self.santaX < 48 else (self.santaX - 10)
            self.coucouY = self.santaY - 8

    def draw(self) :
        if  self.state == Day.STATE_OPENED :
            pyxel.cls(self.color)

        super().draw()

        if  self.state == Day.STATE_OPENED :
            pyxel.blt(self.santaX, self.santaY, 0, 0, 0, 32, 32, 10)
            pyxel.text(self.coucouX, self.coucouY, "coucou", 7)
            if self.coucouX < self.santaX :
                pyxel.line(self.coucouX + 12, self.coucouY + 6, self.coucouX + 13, self.coucouY + 7, 7)
            else :
                pyxel.line(self.coucouX + 11, self.coucouY + 6, self.coucouX + 10, self.coucouY + 7, 7)
            for i in range(128) :
                for j in range(128) :
                    if sqrt((i - pyxel.mouse_x)**2 + (j - pyxel.mouse_y)**2) >= 16 :
                        pyxel.pset(i, j, 0)
