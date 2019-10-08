def x1y1():
    print("You can travel: (N)orth.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            x1y2()
        else:
            print("Not a valid direction!")


def x1y2():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            x1y3()
        elif input_dir == "e" or input_dir == "E":
            status = False
            x2y2()
        elif input_dir == "s" or input_dir == "S":
            status = False
            x1y1()
        else:
            print("Not a valid direction!")


def x1y3():
    print("You can travel: (E)ast or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "e" or input_dir == "E":
            status = False
            x2y3()
        elif input_dir == "s" or input_dir == "S":
            status = False
            x1y2()
        else:
            print("Not a valid direction!")


def x2y1():
    print("You can travel: (N)orth.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            x2y2()
        else:
            print("Not a valid direction!")


def x2y2():
    print("You can travel: (S)outh or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "w" or input_dir == "W":
            status = False
            x1y2()
        elif input_dir == "s" or input_dir == "S":
            status = False
            x2y1()
        else:
            print("Not a valid direction!")


def x2y3():
    print("You can travel: (E)ast or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "e" or input_dir == "E":
            status = False
            x3y3()
        elif input_dir == "w" or input_dir == "W":
            status = False
            x1y3()
        else:
            print("Not a valid direction!")


# If this function is called, "Victory!" gets printed out.
def x3y1():
    print("Victory!")


def x3y2():
    print("You can travel: (N)orth or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            x3y3()
        elif input_dir == "s" or input_dir == "S":
            status = False
            x3y1()
        else:
            print("Not a valid direction!")


def x3y3():
    print("You can travel: (S)outh or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "w" or input_dir == "W":
            status = False
            x2y3()
        elif input_dir == "s" or input_dir == "S":
            status = False
            x3y2()
        else:
            print("Not a valid direction!")


# Asks the user for a direction he wishes to move in.
def inputdir():
    direction = input("Direction: ")
    return direction


# Starts the game with the player in box [1, 1]
x1y1()