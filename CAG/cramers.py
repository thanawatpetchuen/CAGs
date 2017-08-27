from numpy import linalg
from appJar import *
import copy
import string

class Cramers:
    def __init__(self, cramer_number):
        self.cramer_number = cramer_number
        self.A = []
        self.B = []
        self.C = copy.deepcopy(self.A)
        self.T = []
        self.X = []
        self.app = gui("Cramer's Rule Solver By Thanawat", "500x700")
        self.app.setBg("AliceBlue")
        self.app.setFont(18, "Comic Sans")
        self.var_list = []
        self.var_name = []
        self.var_maker()
        self.app.startLabelFrame("Cramer's Rule Solver Program")

        self.app.setSticky("new")

        for row in range(self.cramer_number):
            for column in range(1, self.cramer_number+2):
                self.app.addLabelEntry(self.var_list[(row*(self.cramer_number+1))+column-1], row=row, column=column)
                self.app.setEntryAlign(self.var_list[(row*(self.cramer_number+1))+column-1], "center")
                self.app.setEntryTooltip(self.var_list[(row*(self.cramer_number+1))+column-1]
                                         ,"Example of input formation: X[] ± Y[] ± Z[] ±.... = D[]")

        self.app.addButton("Solve", self.solve, self.cramer_number, 2, colspan=self.cramer_number-1)
        self.app.setButtonBg("Solve", "SteelBlue")
        self.app.setButtonFg("Solve", "White")
        self.app.stopLabelFrame()

        self.app.startLabelFrame("Solution")
        self.app.setSticky("n")
        self.app.addLabel("show_solution", "Solution is")

        for n in range(1, self.cramer_number+1):
            self.app.addEmptyLabel("eq{}".format(n))

        self.app.addEmptyLabel("solution", row=4)
        self.app.stopLabelFrame()

        self.app.enableEnter(self.solve)
        self.app.setFont(18, "Comic Sans")

    def get_entry(self):
        for i in range(self.cramer_number):
            self.A.append([float(self.app.getEntry("{}{}".format(j, i+1))) for j in self.var_name])
            self.B.append(float(self.app.getEntry("D{}".format(i+1))))
        self.C = copy.deepcopy(self.A)

    def var_maker(self):
        xt = self.cramer_number
        name_list = string.ascii_uppercase[string.ascii_uppercase.index("X"):]
        name_list += string.ascii_uppercase[:string.ascii_uppercase.index("X")]
        varlist = []
        label_list = []
        d_list = []
        for n in name_list:
            for i in range(1, xt+1):
                if n != 'D':
                    label_list.append("{}{}".format(n, i))

        for i in range(1, xt+1):
            d_list.append("D{}".format(i))

        label_list = label_list[:xt*xt]
        var_c = []
        for y in range(xt):
            for x in range(y, len(label_list), xt):
                varlist.append(label_list[x])
                var_c.append(label_list[x])
            varlist.append(d_list[y])

        self.var_list = varlist
        self.var_name = list(list(zip(*var_c))[0])[:self.cramer_number]

    def solve(self, btn):
        self.get_entry()
        print(self.A)
        #####################################################################
        for i in range(0, len(self.B)):
            for j in range(0, len(self.B)):
                self.C[j][i] = self.B[j]
                if i > 0:
                    self.C[j][i-1] = self.A[j][i-1]
            self.X.append(round(linalg.det(self.C)/linalg.det(self.A), 1))
        #####################################################################
        self.app.openLabelFrame("Solution")
        self.app.setSticky("new")
        vra = '{}'+" +{}".join(self.var_name) + "= {}"

        for n in range(1, self.cramer_number+1):
            self.app.setLabel("eq{}".format(n), vra.format(*self.A[n-1], self.B[n-1]))

        solut = " = {} ".join(self.var_name) + " = {}"
        self.app.setLabel("solution", solut.format(*self.X))

        self.app.setFg("RoyalBlue")
        self.app.setLabelFg("solution", "DarkGreen")
        self.app.stopLabelFrame()

        self.app.clearAllEntries()
        self.A = []
        self.B = []
        self.C = []
        self.X = []

    def new_input(self, btn):
        self.app.showSubWindow("Input option")

    def app_go(self):
        self.app.go()

