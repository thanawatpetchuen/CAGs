from appJar import *
import copy
import string

class Gauss:
    def __init__(self, gauss_number):
        self.gauss_number = gauss_number
        self.A = []
        self.B = []
        self.C = copy.deepcopy(self.A)
        self.T = []
        self.ans = []
        self.app = gui("Gaussian's Elimination Solver By Thanawat", "500x700")
        self.app.setBg("AliceBlue")
        self.app.setFont(18, "Comic Sans")
        self.var_list = []
        self.var_name = []
        self.var_maker()
        self.app.startLabelFrame("Gaussian's Elimination Solver Program")

        self.app.setSticky("new")

        for row in range(self.gauss_number):
            for column in range(1, self.gauss_number+2):
                self.app.addLabelEntry(self.var_list[(row*(self.gauss_number+1))+column-1], row=row, column=column)
                self.app.setEntryAlign(self.var_list[(row*(self.gauss_number+1))+column-1], "center")
                self.app.setEntryTooltip(self.var_list[(row*(self.gauss_number+1))+column-1]
                                         ,"Example of input formation: X[] ± Y[] ± Z[] ±.... = D[]")

        self.app.addButton("Solve", self.solve, self.gauss_number, 2, colspan=self.gauss_number-1)
        # self.app.addButton("Help", self.help, self.gauss_number+1, 2, colspan=self.gauss_number-1)

        self.app.setButtonBg("Solve", "SteelBlue")
        self.app.setButtonFg("Solve", "White")
        self.app.stopLabelFrame()

        self.app.startLabelFrame("Solution")
        self.app.setSticky("n")
        self.app.addLabel("show_solution", "Solution is")

        for n in range(1, self.gauss_number+1):
            self.app.addEmptyLabel("eq{}".format(n))

        self.app.addEmptyLabel("solution", row=self.gauss_number+1)
        self.app.stopLabelFrame()

        self.app.enableEnter(self.solve)
        self.app.setFont(18, "Comic Sans")

    def help(self, btn):
        self.app.infoBox("Help", "Example of input formation: X[] ± Y[] ± Z[] ±.... = D[]")

    def solve(self, btn):
        self.get_entry()
            # eliminate columns
        for col in range(len(self.A[0])):
            for row in range(col+1, len(self.A)):
                r = [(rowValue * (-(self.A[row][col] / self.A[col][col]))) for rowValue in self.A[col]]
                self.A[row] = [sum(pair) for pair in zip(self.A[row], r)]
            # now backsolve by substitution
        self.A.reverse()  # makes it easier to backsolve
        for sol in range(len(self.A)):
                if sol == 0:
                    self.ans.append(self.A[sol][-1] / self.A[sol][-2])
                else:
                    inner = 0
                    # substitute in all known coefficients
                    for x in range(sol):
                        inner += (self.ans[x]*self.A[sol][-2-x])
                    # the equation is now reduced to ax + b = c form
                    # solve with (c - b) / a
                    self.ans.append((self.A[sol][-1]-inner)/self.A[sol][-sol-2])
        self.ans.reverse()

        self.app.openLabelFrame("Solution")
        self.app.setSticky("new")
        vra = '{}'+" +{}".join(self.var_name) + "= {}"

        for n in range(1, self.gauss_number+1):
            self.app.setLabel("eq{}".format(n), vra.format(*self.T[n-1], self.B[n-1]))

        solut = " = {} ".join(self.var_name) + " = {}"
        self.app.setLabel("solution", solut.format(*self.ans))

        self.app.setFg("RoyalBlue")
        self.app.setLabelFg("solution", "DarkGreen")
        self.app.stopLabelFrame()

        self.app.clearAllEntries()
        self.A = []
        self.B = []
        self.C = []
        self.T = []

    def get_entry(self):
        for i in range(self.gauss_number):
            self.A.append([float(self.app.getEntry("{}{}".format(j, i+1))) for j in self.var_name])
            self.T.append([float(self.app.getEntry("{}{}".format(j, i+1))) for j in self.var_name])
            self.A[i].append(float(self.app.getEntry("D{}".format(i+1))))
            self.B.append(float(self.app.getEntry("D{}".format(i+1))))
        self.C = copy.deepcopy(self.A)

    def var_maker(self):
        xt = self.gauss_number
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
        self.var_name = list(list(zip(*var_c))[0])[:self.gauss_number]

    def app_go(self):
        self.app.go()
