import pyxel
from day import Day

class Day25(Day) :

    def update(self):
        super().update()
        if  self.state == Day.STATE_OPENED :
            # Coder ici
            pass

    def draw(self) :
        if  self.state == Day.STATE_OPENED :
            pyxel.cls(7)
            # Coder ici

        # Affichage fermé ou en ouverture
        if self.state != Day.STATE_OPENED :
            pyxel.rect(self.x, self.y, self.width, self.height, 8)
            pyxel.text(self.x + self.width // 2 - (1 if self.number < 10 else 3), self.y  + self.height // 2 - 2, str(self.number), 7)

        # Affichage ouvert (numéro + bouton)
        else :
            pyxel.text(5, 5, str(self.number), 8)
            pyxel.circb(120, 7, 4, 8)
            pyxel.line(119, 6, 121, 8, 8)
            pyxel.line(121, 6, 119, 8, 8)
