import pyxel
from day import Day

class Day02(Day) :
    
    def __init__(self, x : int, y : int, number : int, color : int, author : str = "") :
        super().__init__(x, y, number, color, "Mathieu")
        song = [
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
        self.song = list()
        for i in range(len(song)) :
            self.song.append(song[i].split(" "))
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
            remainingWords = self.songStep // 10 # Synchro avec la musique 😎
            color = 0
            while remainingWords > 0 and line < len(self.song) :
                prevWordLength = 0
                for i in range(len(self.song[line]) if len(self.song[line]) < remainingWords else remainingWords) :
                    pyxel.text(1 + prevWordLength * 4, 20 + 6 * line, self.song[line][i], color)
                    remainingWords -= 1
                    prevWordLength += len(self.song[line][i]) + 1
                    color += 1
                    if color == 16 :
                        color = 0
                    if color == self.color :
                        color += 1
                line += 1

        super().draw()
