import pyxel
from day import Day
from random import randint
from math import sin

class Day06(Day) :

    def __init__(self, x : int, y : int, number : int, color : int, author : str = "") :
        super().__init__(x, y, number, color, "Mathieu")
        self.steps = 0
        self.stars = []

    def update(self):
        super().update()
        if  self.state == Day.STATE_OPENED :
            self.steps += 1
            
            # Déplacement des étoiles
            for i in range(len(self.stars)) :
                self.stars[i][0] -= 1

            # Ajout d'étoiles
            if self.steps % 2 == 0 :
                # Nettoyage
                if self.steps > 128 : 
                    self.stars.pop(0)
                self.stars.append([127, randint(0, 127)])

    def draw(self) :
        if  self.state == Day.STATE_OPENED :
            pyxel.cls(self.color)
            
            # Affichage des étoiles
            for i in range(len(self.stars)) :
                pyxel.pset(self.stars[i][0], self.stars[i][1], 7)

            # Arrivée de Rudolf
            if self.steps > 107 and self.steps < 128 + 54 :

                # Affichage de l'arc en ciel
                for i in range(self.steps - 128 + 3) :
                    pyxel.pset(i, 67 + sin(self.steps + i), 8)
                    pyxel.pset(i, 68 + sin(self.steps + i), 9)
                    pyxel.pset(i, 69 + sin(self.steps + i), 10)
                    pyxel.pset(i, 70 + sin(self.steps + i), 11)
                    pyxel.pset(i, 71 + sin(self.steps + i), 12)
                    pyxel.pset(i, 72 + sin(self.steps + i), 5)
                
                # Affichage de Rudolf
                pyxel.blt(self.steps - 128, 54 + sin(self.steps), 0, 32, 0, 21, 21, 10)
            
            # Position finale
            elif self.steps >= 128 + 54 :

                for i in range(58) :
                    pyxel.pset(i, 67 + sin(self.steps + i), 8)
                    pyxel.pset(i, 68 + sin(self.steps + i), 9)
                    pyxel.pset(i, 69 + sin(self.steps + i), 10)
                    pyxel.pset(i, 70 + sin(self.steps + i), 11)
                    pyxel.pset(i, 71 + sin(self.steps + i), 12)
                    pyxel.pset(i, 72 + sin(self.steps + i), 5)

                # Affichage de l'arc en ciel
                pyxel.blt(54, 54 + sin(self.steps), 0, 32, 0, 21, 21, 10)

        super().draw()
