import random


# main menu
def display_main_menu():
    print('Welcome, mayor of Simp City!')
    print('----------------------------')
    print('1. Start new game')
    print('2. Load saved game')
    print('3. Show high scores')
    print('0. Exit')


# base board layout
def start_game(buildings, building_count, turn):
    turn = 1

    global board

    board = [['   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ']]
    buildings = building_list * MAX_COUNT  # total amount of buildings available

    for building in building_list:  # loop for diff type of bulding in building list
        building_count[building] = MAX_COUNT  # putting 8(max count) into the dictonary

    print(building_count)  # puts remaining building in a nicer presentation
    return buildings, building_count, turn


# board display with boxes
def display_board(board):

    print('     A     B     C     D')

    print('  +-----+-----+-----+-----+')

    for row in range(NUM_ROWS):
        print(' {}'.format(row + 1), end='')
        for column in range(NUM_COLUMNS):
            print('| {:3s} '.format(board[row][column]), end='')

        print('|')

        print('  ', end='')

        for column in range(1, NUM_COLUMNS + 1):
            print('+-----', end='')
        print('+')


# score section
def showscore():
    row = 1
    column = 1
    houses = []
    highways = []
    shops = []

    beachscore = []
    factorycount = 0
    housescore = []
    shopscore = []
    highwayscore = []
    # scores are empty to be appended for

    for b in board:  # loops board row by row

        for building in b:  # see " "

            if building == "BCH":

                if column == 1 or column == 4:  # a or d
                    beachscore.append(3)  # score + 3
                else:
                    beachscore.append(1)


            elif building == "FAC":
                factorycount = factorycount + 1


            elif building == "HSE":
                houseposition = str(column) + str(row)  # get postion of houses for eg : a1 = 11
                houses.append(houseposition)  # store postion to list

            elif building == "SHP":
                shopposition = str(column) + str(row)
                shops.append(shopposition)

            elif building == "HWY":
                highwayposition = str(column) + str(row)
                highways.append(highwayposition)

            column = column + 1  # at the end of each loop, mopve to next column

        column = 1  # from d back to a

        row = row + 1  # to move to next row

    for house in houses:

        housepoint = 0

        column = int(house[0]) - 1  # index of column for eg a1 - 11 becomes 0
        row = int(house[1]) - 1  # index of row  for eg a1 - 11 becomes 0


        housesaround = []  # store 4 other buildings around it

        # to store up down left right
        if row != 0:
            up = board[row - 1][column]
            housesaround.append(up)

        if row != 3:
            down = board[row + 1][column]
            housesaround.append(down)

        if column != 0:
            left = board[row][column - 1]
            housesaround.append(left)

        if column != 3:
            right = board[row][column + 1]
            housesaround.append(right)

        if "FAC" in housesaround:  # if factory adjacent = 1points regardless
            housescore.append(1)

        else:
            for housearound in housesaround:  # no factory

                if housearound == "HSE" or housearound == "SHP":
                    housepoint = housepoint + 1  # if hse or shp + 1

                elif housearound == "BCH":
                    housepoint = housepoint + 2  # if bch + 2

            housescore.append(housepoint)  # add score to house score / loop if there is another house

        # same as hse till line 139
    for shop in shops:

        column = int(shop[0]) - 1
        row = int(shop[1]) - 1

        shopsaround = []

        if row != 0:

            up = board[row - 1][column]
            shopsaround.append(up)

        if row != 3:
            down = board[row + 1][column]
            shopsaround.append(down)


        if column != 0:
            left = board[row][column - 1]
            shopsaround.append(left)

        if column != 3:
            right = board[row][column + 1]
            shopsaround.append(right)


        # see how many diffrent amount of building around it

        while '   ' in shopsaround:
            shopsaround.remove(
                '   ')  # if checking score mid way and the building around it is empty, remove empty space.

        # remove duplicate in list

        output = []

        for x in shopsaround:  # if buildijng is not in list, it will get added to output list and if it is repeated it will not add.

            if x not in output:
                output.append(x)
        shopscore.append(len(output))  # score = len of output which will be 1 of each building only

    chain = 1


    for highway in highways:

        column = int(highway[0])  # current postion in index
        row = int(highway[1])

        nextcolumn = column + 1  # move to next postion to the right by adding 1 to column index
        nextposition = str(nextcolumn) + str(row)


        if nextposition in highways:  # if next postion is inside highways list which contains index postion of highways
            chain = chain + 1  # add 1 to chain / loop chain will +1 loop till not inside  = get total amounted of connected highways

        else:
            highwayscore.append(chain)
            chain = 1

        # if next postion is not in highways list = add chain into highway score
    totalscore = 0

    print("HSE: ", end='')  # [4, 1, 1, 1, 1]

    if len(housescore) != 0 and len(housescore) != 1:  # if len of housescore is not 0 and is not 1
        for i in range(len(housescore)):

            if i + 1 == len(housescore):  # if is at last item it will print = instead of +
                print(str(housescore[i]) + " = ", end='')
            else:
                print(str(housescore[i]) + " + ", end='')

    print(sum(housescore))
    totalscore = totalscore + sum(housescore)

    print("SHP: ", end='')  # [3, 2]

    if len(shopscore) != 0 and len(shopscore) != 1:

        for i in range(len(shopscore)):

            if i + 1 == len(shopscore):
                print(str(shopscore[i]) + " = ", end='')
            else:
                print(str(shopscore[i]) + " + ", end='')

    print(sum(shopscore))

    totalscore += sum(shopscore)
    print("HWY: ", end='')  # [1, 1, 1]

    total = 0
    operation = " + "

    if len(highwayscore) == 1:  # if highway only have 1 - dont need anything else just 1 point
        print(1)
        totalscore = totalscore + 1

    else:
        for i in range(len(highwayscore)):

            if i + 1 == len(highwayscore):  # if at the last of the list end with  =
                operation = " = "
            if highwayscore[i] == 1:  # if in the middle of the list end with +
                print("1" + operation, end='')
                total += 1  # add 1 to the score
            else:
                for j in range(highwayscore[i]):  # for connect highways will loop the amount of connected
                    print(str(highwayscore[i]) + operation,
                          end='')  # print amount of connected highway ending with as plus
                    total += highwayscore[i]  # add the connected highways score

        print(total)
        totalscore = totalscore + total

    print("FAC: ", end="")

    if factorycount == 0:  # 5
        print(0)

    elif factorycount == 1:
        print(1)

    elif factorycount <= 4:

        for i in range(factorycount):

            if i + 1 == factorycount:
                print(str(factorycount) + " = ", end='')

            else:
                print(str(factorycount) + " + ", end='')
        print(factorycount ** 2)  # 2-4 fact = number of fact square

    else:  # more than 4

        for i in range(4):  # 4 + 4 + 4 + 4
            print("4 + ", end='')
        factorycount = factorycount - 4
        total = 16 + factorycount  # if there is 5 /  5 -4 = 1 left 4**2 + 1

        for i in range(factorycount):

            if i + 1 == factorycount:
                print("1 = ", end='')
            else:
                print("1 + ", end='')

        print(total)
    totalscore += total

    print("BCH: ", end='')
    # score for beach caulcuate ontop , list will show score of each beach

    if len(beachscore) == 1:  # [3] if only one in the list
        print(beachscore[0])

    else:
        i = 0

        while i < len(beachscore):  # [3]


           if i + 1 == len(beachscore):
                print(str(beachscore[i]) + " = ", end='')

           else:
                print(str(beachscore[i]) + " + ", end='')

           i += 1
        print(sum(beachscore))

    totalscore += sum(beachscore)
    print("Total score: " + str(totalscore))  # to show total score

    return totalscore


def savegame():

    file1 = open("myfile.txt", "w")  # open file and write

    for row in board:

        for item in row:

            if item == '   ':  # if space in board is empty file will write EMPTY and move to next line
                file1.write("EMPTY")
                file1.write("\n")

            else:
                file1.write(item)  # file will write item in space on the board and move to next line
                file1.write("\n")

    file1.close()  # to close file


def readhighscore():

    global topscore

    topscore = []
    file1 = open('score.txt', 'r')  # openfile and read
    Lines = file1.readlines()  # read line by line

    for line in Lines:  # loops line by line
        topscore.append(line.strip().split("\t"))  # remove \n and split to a list


def highscore(userscore):

    global topscore

    if topscore == []:
        print("Congratulations! You made the high score board at position 1!")

        username = input("Please enter your name (max 20 chars): ")

        topscore.append([username, userscore])

        file1 = open("score.txt", "w")

        file1.write(username + "\t" + str(userscore))
        file1.write("\n")
        file1.close()
        readhighscore()  # update global top score
    else:
        #[["Dom", 20], ["Branson" ,25]]
        tenthplacescore = topscore[0][1]

        ranking = len(topscore) + 1

        index = 0

        if len(topscore) < 10 or userscore > int(tenthplacescore):

            for topscorer in topscore:

                if userscore > int(topscorer[1]): #to loop to check if current score higher than moving forwardplace score
                    ranking = ranking - 1
                    index = index + 1 #to see where to put in the list
                else:
                    break
            print("Congratulations! You made the high score board at position {}!".format(ranking))

            username = input("Please enter your name (max 20 chars): ")
            topscore.insert(index, [username, userscore])

            file1 = open("score.txt", "w")

            for row in topscore:
                file1.write(row[0] + "\t" + str(row[1]))
                file1.write("\n")
            file1.close()
            readhighscore()  # update global top score


def showtopscore():
    print("--------- HIGH SCORES ---------")
    print('{:2s} {:21s} {:20s} '.format('Pos', 'Player', 'Score'))
    print('{:2s} {:21s} {:20s}'.format('---', "------", "-----"))
    position = 1

    for player in reversed(topscore):
        print('{:2}. {:24s} {:20}'.format(position, player[0], player[1]))
        position += 1
    print("-------------------------------")


def play_game(buildings, building_count, turn):
    global board  # global board = updated board and saved every loop
    display_board(board)

    choice = -1

    while choice != 0:

        building1 = buildings[random.randint(0, len(buildings) - 1)]
        building2 = buildings[random.randint(1, len(buildings) - 2)]

        print('1. Build a {}'.format(building1))
        print('2. Build a {}'.format(building2))
        print('3. See remaining Buildings')
        print('4. See current score')
        print('5. Save game')
        print('0. Exit to main menu')
        choice = input('Your Choice? ')
        letters = ["A", "B", "C", "D"]
        rows = ['1', '2', '3', '4']

        if choice == '1':

            while True: #continue loppoing untill there is a proper postion
                position = (input("Build where? "))

                if len(position) != 2: #must be 2 things
                    print("Error! Invalid Position")
                    continue
                column = position[0].upper()  # uppercase the alpha
                row = position[1]

                if column not in letters or row not in rows: #make sure columm is abcd and rows is 1234
                    print("Error! Invalid Position")
                    continue
                column = letters.index(column) + 1  # compares the alpha to the list

                if board[int(row) - 1][column - 1] != '   ': #if box is not empty , mean there is a building filled already
                    print("Error! Position already filled")

                else:
                    break   #if no error, break otherwise it will continue looping

            board[int(row) - 1][column - 1] = building1  # eg a1 columm and row  = 1,1 in board to access space is 0,0 so -1
            building_count[building1] = building_count[building1] - 1 #to minus 1 building of the building placed

            if turn == 16:
                print("Final layout of Simp City:")
                display_board(board)
                userscore = showscore()
                highscore(userscore)
                showtopscore()
                break

            else:
                print(building_count)
                print("Turn %d \n" % (turn + 1))
                display_board(board)
            turn = turn + 1

        elif choice == '2':

            while True:
                position = (input("Build where? "))

                if len(position) != 2:
                    print("Error! Invalid Position")
                    continue
                column = position[0].upper()  # uppercase the alpha
                row = position[1]

                if column not in letters or row not in rows:
                    print("Error! Invalid Position")
                    continue
                column = letters.index(column) + 1  # compares the alpha to the list

                if board[int(row) - 1][column - 1] != '   ':
                    print("Error! Position already filled")

                else:
                    break
            board[int(row) - 1][column - 1] = building2
            building_count[building2] = building_count[building2] - 1
            turn = turn + 1

            if turn - 1 == 16:
                print("Final layout of Simp City:")
                display_board(board)
                userscore = showscore()
                highscore(userscore)
                showtopscore()
                break

            else:
                print(building_count)
                print("Turn %d \n" % (turn + 1))
                display_board(board)

        elif choice == '3':
            print(building_count)
            print('{:15s} {:15s} '.format('Building', 'Remaining'))
            print('{:15s} {:15s} '.format('--------', "---------"))
            for building in building_count:
                print('{:8s} {:8} '.format(building, building_count[building]))


        elif choice == '4':
             showscore()

        elif choice == '5':
            savegame()
            print("Game saved!")
            break

        elif choice == '0':
            break

        else:
            print("Error! Invalid option!")



# 1.2.    Load Saved Game
def load_game(buildings, building_count, turn):
    '''
    open and read data from a file
    '''
    global board

    file1 = open('myfile.txt', 'r')  # openfile
    Lines = file1.readlines()  # read line by line
    count = 0

    for line in Lines:  # loops line by line
        row = count // 4
        column = count % 4
        # count = 0 eg for a1 row - 0 //4 = 0 / 0 % 4 = 0 / a1 = 00 / b1 - 1//4 = 0 / 1%4 = 1 b1 =01
        if line.strip() == "EMPTY":  # strip get rids of \n
            board[row][column] = '   '  # leaves empty if no saved building

        else:
            board[row][column] = line.strip()  # prints building in board
            building_count[line.strip()] -= 1 #to minus building
            turn += 1
        count += 1

    return buildings, building_count, turn


def display_remaining_buildings():
    pass


def display_currect_score():
    pass


board = []
buildings = []
building_count = {}
building_list = ['HSE', 'FAC', 'SHP', 'HWY', 'BCH']
MAX_COUNT = 8
NUM_ROWS = 4
NUM_COLUMNS = 4
turn = 1
option = -1
topScore = []
readhighscore()

while option != 0:
    display_main_menu()
    option = input('Your choice? ')

    if option == '0':
        print(" Thank you for playing")
        break

    elif option == '1':
        ''' Start new game '''
        buildings, building_count, turn = start_game(buildings, building_count, turn)
        play_game(buildings, building_count, turn)

    elif option == '2':
        ''' Load saved game '''
        print('This loads saved game')
        buildings, building_count, turn = start_game(buildings, building_count, turn)
        buildings, building_count, turn = load_game(buildings, building_count, turn)
        play_game(buildings, building_count, turn)

    elif option == '3':
        showtopscore()

    else:

        print("Error! Invalid option!")

