import pyxel
from day import Day

class Day05(Day) :

    def __init__(self, x : int, y : int, number : int, color : int, author : str = "") :
        super().__init__(x, y, number, color, "Mathieu")
        self.steps = 0
        self.increasing = 1
        self.scale = 0
        self.rotation = 0

    def update(self):
        super().update()
        if  self.state == Day.STATE_OPENED :
            self.steps += 1
    
            # On augmente/diminue la taille toutes les 3 étapes 
            if self.steps % 3 == 0 :
                self.scale = self.scale + self.increasing
            
            # On change le sens (augmentation/diminution toutes les 200 étapes)
            if self.steps % 200 == 0 :
                self.increasing = - self.increasing
            
            # On tourne de 3° à chaque étape
            self.rotation = self.steps * 3

    def draw(self) :
        if  self.state == Day.STATE_OPENED :
            pyxel.cls(self.color)
            
            # Affichage du Père Noël
            pyxel.blt(48, 48, 0, 0, 0, 32, 32, 10, rotate = self.rotation, scale = self.scale * 0.1)

        super().draw()
