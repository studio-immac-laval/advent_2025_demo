import pyxel
from day import Day

class Day14(Day) :

    def update(self):
        super().update()
        if  self.state == Day.STATE_OPENED :
            # Coder ici
            pass

    def draw(self) :
        if  self.state == Day.STATE_OPENED :
            pyxel.cls(self.color)
            # Coder ici

        super().draw()
