class Pion:
    def __init__(self, axex, axey, equipe):
        self.axex = axex
        self.axey = axey
        self.equipe = equipe

    def changeequipe(self, equipe):
        if equipe == ' X':
            equipe = ' O'
        elif equipe == ' O':
            equipe = ' X'
