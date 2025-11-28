import pyxel
from day import Day

class Day01(Day) :

    def __init__(self, x : int, y : int, number : int, color : int, author : str = "") :
        super().__init__(x, y, number, color, "Mathieu")
        self.song = [
            "Vive le vent,",
            "Vive le vent,",
            "Vive le vent d'hiver",
            "Qui s'en va sifflant, soufflant,",
            "Dans les grands sapins verts...",
            "Hey !",
            " ",
            "Vive le temps,",
            "Vive le temps,",
            "Vive le temps d'hiver",
            "Boule de neige et jour de l'an,",
            "Et bonne annee grand-mere !"
        ]
        self.songStep = 0
        self.songDisplay = False

    def update(self):
        super().update()
        if  self.state == Day.STATE_OPENING :
            self.songStep = 0
        if  self.state == Day.STATE_OPENED :
            if self.songStep == 0 :
                self.songDisplay = True
                pyxel.playm(0)
            self.songStep += 1


    def draw(self) :
        if  self.state == Day.STATE_OPENED :
            pyxel.cls(self.color)
            line = 0
            remainingChars = self.songStep // 2 # Synchro avec la musique 😎
            while remainingChars > 0 :
                if remainingChars < len(self.song[line]) :
                    pyxel.text(1, 20 + 7 * line, self.song[line][:remainingChars], 7)
                    remainingChars = 0
                else :
                    pyxel.text(1, 20 + 7 * line, self.song[line], 7)
                    remainingChars -= len(self.song[line])
                    line += 1
                    if line == len(self.song) :
                        line -= 1
                        self.songDisplay = False

        super().draw()
