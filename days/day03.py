import pyxel
from random import randint
from day import Day

class SnowFlake :
    def __init__(self):
        self.x = randint(0, 127)
        self.y = 0

    def update(self) :
        if pyxel.pget(self.x, self.y + 1) != 7 and self.y < 127 :
            self.y += 1

    def draw(self) :
        pyxel.pset(self.x, self.y, 7)

class Day03(Day) :
    
    def __init__(self, x : int, y : int, number : int, color : int, author : str = "") :
        super().__init__(x, y, number, color, "Mathieu")
        self.snow = []

    def update(self):
        super().update()
        if  self.state == Day.STATE_OPENING :
            del self.snow[:]
            self.snow = []
        if  self.state == Day.STATE_OPENED :
            
            # On limite le nombre de flocons
            if (len(self.snow) < 128 * 64) :
                # Ajouter des flocons
                for i in range(randint(3, 10)) :
                    self.snow.append(SnowFlake())
            
            # Mettre à jour les flocons
            for i in range(len(self.snow)) :
                self.snow[i].update()

    def draw(self) :
        if  self.state == Day.STATE_OPENED :
            pyxel.cls(self.color)
            # Dessiner les flocons
            for i in range(len(self.snow)) :
                self.snow[i].draw()

        super().draw()
