from appJar import *
from Homework.Main.CAG import cramers
from Homework.Main.CAG import gaussian

class Mainmenu:
    def __init__(self):
        self.app = gui("CAG Version 1", "300x250")
        self.app.setBg("AliceBlue")
        self.app.setResizable(canResize=False)
        self.app.setLocation(500, 500)
        self.app.startLabelFrame("Main Menu")
        self.app.setSticky("nswe")
        self.app.setFont("18")
        self.app.addButton("Cramer's Rule", self.go_cramer, row=1, column=2, colspan=2)
        self.app.addButton("Gaussian's Elimination", self.go_gaussian, row=2, column=2, colspan=2)
        self.app.setButtonTooltip("Cramer's Rule", "This function will calculate the answer by Cramer's Rule")
        self.app.setButtonTooltip("Gaussian's Elimination",
                                  "This function will calculate the answer by Gaussian's Elimination")
        self.app.setButtonWidth("Gaussian's Elimination", "50")
        self.app.stopLabelFrame()
        self.cramers_number = 0

    def app_go(self):
        self.app.go()

    def go_cramer(self, btn):
        cramer_number = self.app.numberBox("Input your number", "How many dimension do you want?")
        cramerss = cramers.Cramers(cramer_number)
        cramerss.app_go()

    def go_gaussian(self, btn):
        gauss_number = self.app.numberBox("Input your number", "How many dimension do you want?")
        gaussiann = gaussian.Gauss(gauss_number)
        gaussiann.app_go()
        
