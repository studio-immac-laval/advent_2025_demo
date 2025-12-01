import pyxel
from day import Day

class Day04(Day) :

    def __init__(self, x : int, y : int, number : int, color : int, author : str = "") :
        super().__init__(x, y, number, color, "Mathieu")
        self.steps = 0

    def update(self):
        super().update()
        if  self.state == Day.STATE_OPENED :
            self.steps += 1

    def draw(self) :
        if  self.state == Day.STATE_OPENED :
            
            pyxel.cls(self.color)
            
            # Ligne par ligne
            for y in range(21) :

                # Caractère par caractère
                for x in range(33) :

                    pyxel.text(
                        -4 + x * 4 + ((-1 * self.steps % 5) if y % 2 == 0 else (self.steps % 5)), # Une ligne sur deux on recule/avance de 0 à 4 pixels à chaque étape
                        1 + y * 6, 
                        str(y % 10), 
                        14
                    )

        super().draw()
