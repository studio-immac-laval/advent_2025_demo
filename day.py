import pyxel 

class Day :

    STATE_CLOSED  = 0
    STATE_OPENING = 1
    STATE_OPENED  = 2

    WIDTH  = 15
    HEIGHT = 15
    
    OPENING_STEPS = 20

    def __init__(self, x : int, y : int, number : int, color : int, author : str = "") :
        self.origX = x
        self.origY = y
        self.x = x
        self.y = y
        self.width  = Day.WIDTH
        self.height = Day.HEIGHT
        
        # Attributs pour le zoom
        self.dx = self.x / Day.OPENING_STEPS
        self.dy = self.y / Day.OPENING_STEPS
        self.dw = (128 - (self.x + 15)) / Day.OPENING_STEPS
        self.dh = (128 - (self.y + 15)) / Day.OPENING_STEPS
        
        self.number = number
        self.color = color
        self.author = author
        
        self.state = Day.STATE_CLOSED
        self.animationStep = 0

    def update(self) :
        # Détection du clic d'ouverture
        if self.state == Day.STATE_CLOSED and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.x <= pyxel.mouse_x < self.x + 13 and self.y <= pyxel.mouse_y < self.y + 13 :
            self.state = Day.STATE_OPENING

        # Ouverture
        if self.state == Day.STATE_OPENING : 
            self.animationStep += 1
            self.x -= self.dx
            self.y -= self.dy
            self.width += self.dw + self.dx
            self.height += self.dh + self.dy
            # Fin d'ouverture
            if self.animationStep == Day.OPENING_STEPS :
                self.state = Day.STATE_OPENED
                self.x = self.origX
                self.y = self.origY
                self.width  = Day.WIDTH
                self.height = Day.HEIGHT
                self.animationStep = 0

        # Fermeture
        if self.state == Day.STATE_OPENED and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 116 <= pyxel.mouse_x <= 124 and 3 <= pyxel.mouse_y <= 11 :
            self.state = Day.STATE_CLOSED

    def draw(self) :
        # Affichage fermé ou en ouverture
        if self.state != Day.STATE_OPENED :
            pyxel.rect(self.x, self.y, self.width, self.height, 7)
            pyxel.rectb(self.x, self.y, self.width, self.height, self.color)
            pyxel.text(self.x + self.width // 2 - (1 if self.number < 10 else 3), self.y  + self.height // 2 - 2, str(self.number), self.color)

        # Affichage ouvert (numéro + bouton)
        else :
            pyxel.text(5, 5, str(self.number), 7)
            pyxel.circb(120, 7, 4, 7)
            pyxel.line(119, 6, 121, 8, 7)
            pyxel.line(121, 6, 119, 8, 7)
            if self.author != "" :
                pyxel.text(5, 118, "@" + self.author, 7)