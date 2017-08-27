from Homework.Main.CAG.mainmenu import *
from appJar import *

def __init__():
    app = gui("Welcome to CAG")
    app.setResizable(canResize=False)
    app.setBg("DodgerBlue")
    app.setFg("White")

    def press(btnName):
        if btnName == "Cancel":
            app.stop()
            return

        if app.getEntry("userEnt") == "thanawat":
            if app.getEntry("passEnt") == "petchuen":
                app.infoBox("Success", "Congratulations, you are logged in!")
                app.stop()
                mainmenu = Mainmenu()
                mainmenu.app_go()

            else:
                app.errorBox("Failed login", "Invalid password")
        else:
            app.errorBox("Failed login", "Invalid username")

    app.setSticky("ewn")
    # add labels & entries
    # in the correct row & column
    app.addLabel("userLab", "Username:", 0, 0)
    app.addEntry("userEnt", 0, 1)
    app.addLabel("passLab", "Password:", 1, 0)
    app.addSecretEntry("passEnt", 1, 1)

    # changed this line to call a function
    app.addButtons( ["Submit", "Cancel"], press, colspan=2)

    # add some enhancements
    app.setFocus("userEnt")
    app.enableEnter(press)

    # start the GUI
    app.go()


if __name__ == '__main__':
    __init__()

