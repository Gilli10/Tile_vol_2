coins = 0

def x1y1(coins):
    print("You can travel: (N)orth.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            x1y2(coins)
        else:
            print("Not a valid direction!")


def x1y2(coins):
    pull_lever(coins)
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            x1y3(coins)
        elif input_dir == "e" or input_dir == "E":
            status = False
            x2y2(coins)
        elif input_dir == "s" or input_dir == "S":
            status = False
            x1y1(coins)
        else:
            print("Not a valid direction!")


def x1y3(coins):
    print("You can travel: (E)ast or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "e" or input_dir == "E":
            status = False
            x2y3(coins)
        elif input_dir == "s" or input_dir == "S":
            status = False
            x1y2(coins)
        else:
            print("Not a valid direction!")


def x2y1(coins):
    print("You can travel: (N)orth.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            x2y2(coins)
        else:
            print("Not a valid direction!")


def x2y2(coins):
    pull_lever(coins)
    print("You can travel: (S)outh or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "w" or input_dir == "W":
            status = False
            x1y2(coins)
        elif input_dir == "s" or input_dir == "S":
            status = False
            x2y1(coins)
        else:
            print("Not a valid direction!")


def x2y3(coins):
    pull_lever(coins)
    print("You can travel: (E)ast or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "e" or input_dir == "E":
            status = False
            x3y3(coins)
        elif input_dir == "w" or input_dir == "W":
            status = False
            x1y3(coins)
        else:
            print("Not a valid direction!")


# If this function is called, "Victory!" gets printed out.
def x3y1(coins):
    print("Victory! Total coins",coins)


def x3y2(coins):
    pull_lever(coins)
    print("You can travel: (N)orth or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            x3y3(coins)
        elif input_dir == "s" or input_dir == "S":
            status = False
            x3y1(coins)
        else:
            print("Not a valid direction!")


def x3y3(coins):
    print("You can travel: (S)outh or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "w" or input_dir == "W":
            status = False
            x2y3(coins)
        elif input_dir == "s" or input_dir == "S":
            status = False
            x3y2(coins)
        else:
            print("Not a valid direction!")


# Asks the user for a direction he wishes to move in.
def inputdir():
    direction = input("Direction: ")
    return direction

def pull_lever(coins):
    anwser = input("Pull a lever (y/n): ")
    if anwser == "y" or anwser == "Y":
        coins +=1
        print("You received 1 coin, your total is now {}.".format(coins))



# Starts the game with the player in box [1, 1]
x1y1(coins)
