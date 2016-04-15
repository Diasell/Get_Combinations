import random

REEL_SET0 = [[1,7,8,0,5,8,7,2,4,9,2,5,8,1,2,4,5,3,0,6,5,4,8,10,1,6,7,1,6,2,4,5,3,1,8,6,3,4,1,0,5,4,8,3,1,5,3,6,8,10,0,4,1,2,3,1,7,2,1,4,0,6,5,4,7,3,0,2,7,1,3,5,4,2,10,1,3,2,7,4,3,8,4,3,6,2,3,4,5,6,2,1,5,3,7,2,5,1,7,3,9,5,2,4,1,3,2,1,6,7,2,1,8,4,6,0,3,7,1,3,2,6,1,2,10,5,4,2,6],
             [3,1,0,8,2,0,3,6,2,7,4,2,1,4,3,1,5,3,2,4,5,6,7,0,1,4,0,7,2,1,5,8,1,6,2,3,6,5,1,8,5,2,6,1,2,7,1,5,7,2,4,1,5,6,2,5,7,4,1,2,7,3,2,1,8,2,1,3,5,4,9,5,4,3,8,4,3,9,1,7,3,1,0,5,1,3,6,5,1,4,8,1,3,6,2,7,4,0,6,4,2,6,7,1,2,4,6,3,9,2,3,7,6,3,4,2,5,1,2,3,8,5,3,4,8,3,4,2],
             [4,6,1,2,5,4,6,3,4,1,3,7,6,4,2,6,1,3,8,5,2,4,6,1,7,4,2,1,3,2,5,7,2,6,7,8,3,1,4,9,8,0,3,1,8,4,5,2,6,8,5,0,6,3,7,1,2,4,0,6,3,1,2,4,3,7,0,3,1,5,9,4,3,2,1,5,0,1,5,3,4,1,2,5,1,2,3,8,2,5,4,3,0,9,7,1,4,7,2,4,5,8,1,3,7,2,1,7,6,5,2,6,1,3,6,5,2,3,1,2,8,1,2,5,4,3,7,2],
             [3,6,9,8,4,3,6,4,2,6,0,2,7,3,2,8,1,0,6,4,2,5,7,1,2,7,3,1,9,8,2,7,4,2,5,7,8,3,5,2,8,3,0,2,7,4,1,2,6,1,5,9,0,6,1,4,5,1,2,6,3,4,1,0,5,6,8,4,5,1,2,0,3,5,2,1,3,6,7,3,1,4,2,5,7,1,3,4,1,3,2,4,1,5,4,1,3,2,8,6,5,1,6,7,1,8,6,1,5,3,2,4,3,2,7,1,3,4,7,3,5,1,3,2,4,1,2,4],
             [3,1,6,7,1,6,7,2,5,1,3,7,6,8,5,6,1,2,5,4,10,1,5,7,6,0,5,6,4,1,3,8,0,3,4,1,3,5,0,4,2,5,3,7,2,4,3,8,1,7,6,1,9,4,5,2,8,4,2,7,3,4,10,2,1,3,2,5,9,1,4,0,2,1,3,2,4,6,1,5,0,2,1,3,10,1,4,2,6,3,0,2,5,6,9,2,4,5,3,2,1,8,3,2,1,3,2,8,3,2,1,7,4,8,2,1,4,3,10,1,2,4,8,5,3,1,6,7,4]]

REEL_SET1 = [[5, 0, 7, 3, 6, 8, 3, 6, 1, 6, 3, 10, 9, 7, 5, 0, 6, 10, 8, 5, 10, 1, 9, 6, 1, 1, 8, 0, 9, 3, 1, 2, 0, 8, 7, 8, 7, 1, 3, 1, 9, 7, 0, 3, 9, 10, 1, 3, 7, 5, 5, 9, 9, 10, 10, 4, 2, 8, 0, 1, 9, 7, 2, 1, 4, 0, 0, 6, 8, 10, 2],
             [6, 6, 3, 0, 6, 4, 2, 3, 10, 10, 9, 7, 1, 7, 10, 6, 4, 0, 8, 5, 2, 7, 8, 8, 10, 2, 2, 5, 5, 8, 0, 8, 2, 1, 5, 0, 10, 3, 7, 10, 0, 5, 4, 4, 5, 7, 7, 0, 1, 9, 3, 5, 4, 7, 9, 6, 3, 5, 5, 1, 5, 5, 1, 0, 2, 2, 1, 0, 7, 2, 3, 4],
             [3, 2, 1, 1, 6, 9, 10, 7, 10, 10, 4, 0, 7, 7, 6, 2, 0, 8, 10, 2, 9, 4, 2, 8, 1, 6, 10, 10, 3, 10, 3, 8, 8, 0, 0, 1, 7, 0, 8, 1, 6, 9, 7, 0, 0, 1, 0, 0, 8, 7, 2, 1, 2, 0, 6, 2, 1, 7, 2, 4, 5, 8, 0, 8, 2, 0, 9, 1, 10, 5, 1, 8],
             [3, 9, 7, 0, 0, 10, 1, 10, 2, 9, 7, 9, 8, 7, 5, 7, 5, 3, 8, 2, 5, 9, 8, 1, 6, 4, 4, 8, 9, 5, 3, 3, 8, 0, 2, 6, 2, 9, 7, 2, 5, 4, 10, 6, 1, 10, 8, 8, 7, 2, 0, 8, 3, 9, 5, 7, 7, 9, 10, 10, 0, 4, 10, 9, 5, 4, 6, 2, 3, 0],
             [7, 9, 1, 5, 2, 7, 1, 4, 5, 3, 0, 7, 0, 2, 1, 6, 9, 6, 7, 0, 7, 0, 2, 6, 9, 7, 0, 6, 5, 4, 8, 9, 7, 4, 2, 8, 5, 5, 3, 2, 6, 8, 7, 4, 0, 7, 6, 7, 9, 4, 4, 2, 2, 4, 4, 6, 0, 8, 1, 4, 0, 5, 8, 8, 7, 8, 2, 2, 6, 3]]

REEL_SET2 = [[0, 2, 2, 4, 5, 3, 4, 7, 4, 4, 3, 3, 2, 3, 1, 0, 2, 8, 5, 7, 3, 10, 9, 0, 1, 10, 3, 7, 9, 3, 10, 7, 1, 7, 5, 7, 9, 3, 9, 5, 10, 0, 8, 0, 2, 9, 2, 8, 3, 6, 0, 8, 0, 3, 2, 3, 0, 4, 2, 2, 0, 3, 5, 10, 6, 4, 6, 10, 4, 5, 0, 10],
             [4, 0, 2, 3, 3, 1, 6, 3, 2, 0, 8, 10, 7, 4, 5, 6, 2, 8, 8, 6, 0, 10, 4, 5, 9, 10, 5, 0, 2, 5, 4, 2, 4, 10, 8, 0, 3, 5, 10, 6, 2, 5, 7, 4, 2, 0, 2, 0, 6, 8, 1, 1, 7, 1, 6, 3, 2, 8, 6, 10, 1, 1, 5, 0, 10, 3, 5, 6, 6, 1, 4, 4],
             [7, 2, 7, 7, 4, 0, 6, 1, 7, 3, 2, 1, 10, 9, 5, 5, 2, 9, 6, 2, 5, 1, 6, 3, 3, 8, 8, 9, 3, 10, 7, 1, 10, 9, 7, 8, 0, 2, 2, 4, 10, 1, 3, 6, 10, 5, 6, 2, 0, 6, 4, 5, 8, 5, 10, 3, 4, 6, 3, 2, 0, 3, 10, 8, 2, 8, 9, 5, 4, 3, 10, 3, 9],
             [2, 6, 4, 10, 7, 5, 3, 9, 4, 7, 8, 3, 5, 10, 9, 2, 6, 3, 1, 6, 1, 8, 0, 4, 10, 2, 1, 2, 3, 3, 6, 2, 5, 6, 5, 9, 2, 7, 1, 3, 6, 8, 8, 5, 8, 7, 0, 10, 10, 9, 6, 6, 6, 7, 3, 8, 4, 3, 5, 10, 5, 0, 1, 1, 0, 9, 5, 8, 10, 5, 10, 10, 10, 1],
             [7, 4, 3, 4, 6, 9, 3, 3, 1, 5, 3, 0, 6, 3, 6, 0, 6, 2, 0, 8, 5, 6, 1, 4, 3, 1, 8, 4, 2, 2, 6, 10, 5, 0, 0, 5, 5, 2, 7, 9, 5, 10, 8, 10, 0, 2, 7, 1, 5, 4, 5, 5, 9, 0, 2, 5, 9, 9, 9, 1, 0, 0, 8, 7, 2, 1, 2, 0, 6, 2, 5, 10, 4]]

ALL_REEL_SETS = [REEL_SET0, REEL_SET1, REEL_SET2]

# Symbols:
WILD        = 9
GREEN_WITCH = 6
BLUE_WITCH  = 8
RED_WITCH   = 7
CAT         = 5
SKULL       = 3
CROW        = 4
AMULET      = 1
POISON      = 2
SCATTER     = 0
BONUS       = 10
list_of_symbols = range(11)

# Winning Lines:
LINE1  = [1,1,1,1,1]
LINE2  = [2,2,2,2,2]
LINE3  = [0,0,0,0,0]
LINE4  = [0,1,2,1,0]
LINE5  = [2,1,0,1,2]
LINE6  = [1,0,0,0,1]
LINE7  = [1,2,2,2,1]
LINE8  = [0,0,1,2,2]
LINE9  = [2,2,1,0,0]
LINE10 = [1,0,1,2,1]
LINE11 = [1,2,1,0,1]
LINE12 = [0,1,1,1,0]
LINE13 = [2,1,1,1,2]
LINE14 = [0,1,0,1,0]
LINE15 = [2,1,2,1,2]
LINE16 = [1,1,0,1,1]
LINE17 = [1,1,2,1,1]
LINE18 = [0,0,2,0,0]
LINE19 = [2,2,0,2,2]
LINE20 = [0,2,2,2,0]

LINES = [LINE1,LINE2,LINE3,LINE4,LINE5,LINE6,LINE7,LINE8,LINE9,LINE10,LINE11,
         LINE12,LINE13,LINE14,LINE14,LINE15,LINE16,LINE17,LINE18,LINE19,LINE19,LINE20]

def userinput(topline, middleline, bottomline):
    reelcombination = [[],[],[],[],[]]
    lineup   = topline.split(" ")
    linemid  = middleline.split(" ")
    linedown = bottomline.split(" ")
    for index in range(len(lineup)):
        reelcombination[index].append(int(lineup[index]))
    for index in range(len(linemid)):
        reelcombination[index].append(int(linemid[index]))
    for index in range(len(linedown)):
        reelcombination[index].append(int(linedown[index]))
    return reelcombination


def if3symbols(symbol1, symbol2, symbol3, reel):
    """
    returns TRUE/FALSE if such combination exists
    """
    for i in range(len(reel)-3):
        if  reel[i] == symbol1 and reel[i+1] == symbol2 and reel[i+2] == symbol3:
            return True
    return False


def if2symbols(symbol1, symbol2, reel):
    """
    returns TRUE/FALSE if such combination exists
    """
    for i in range(len(reel)-2):
        if  reel[i] == symbol1 and reel[i+1] == symbol2:
            return True
    return False


def find3symbols(symbol1, symbol2, symbol3, reel):
    """
    returns a positon of the combination on the reel(index of the first symbol in the reel list)
    """
    for i in range(len(reel)-3):
        if  reel[i] == symbol1 and reel[i+1] == symbol2 and reel[i+2]== symbol3:
            return i


def find2symbols(symbol1, symbol2, reel):
    """
    returns a positon of the combination on the reel(index of the first symbol in the reel list)
    """
    for i in range(len(reel)-2):
        if  reel[i] == symbol1 and reel[i+1] == symbol2:
            return i


def find1symbols(symbol, reel):
    """
    returns a positon of the symbol on the reel
    """
    for i in range(len(reel)):
        if  reel[i] == symbol:
            return i



def loopreelset(combination, reel_set):
    """
    Loops through given reel set and give TRUE/FALSE whether combination with 3 symbols on the each reel is possible
    """
    matching_reels = []
    for index in range(5):
        if if3symbols(combination[index][0],combination[index][1],combination[index][2], reel_set[index]):
            matching_reels.append(index)
    if len(matching_reels) == 5:
        return True


def loopreelset2(combination, reel_set):
    """
    Loops through given reel set and give TRUE/FALSE whether combination with 2 symbols on each reel is possible
    """
    matching_reels = []
    for index in range(5):
        if if2symbols(combination[index][0],combination[index][1], reel_set[index]):
            matching_reels.append(index)
    if len(matching_reels) == 5:
        return True


def gettestcase(combination):
    testcase = []
    reelset_index = 0
    while reelset_index<len(ALL_REEL_SETS):
        reel_set = ALL_REEL_SETS[reelset_index]
        if loopreelset(combination, reel_set):
            testcase.append(reelset_index)
            for reel in range(len(reel_set)):
                testcase.append(find3symbols(combination[reel][0], combination[reel][1], combination[reel][2], reel_set[reel]))
            return testcase

        elif loopreelset2(combination, reel_set):
            testcase.append(reelset_index)
            for reel in range(len(reel_set)):
                testcase.append(find2symbols(combination[reel][0], combination[reel][1], reel_set[reel]))
            return testcase
        reelset_index +=1


def getAllSymbolsFromReel(symbol, reel):
    allsymbolsets = []
    for i in range(len(reel)-3):
        symbolset =[]
        if reel[i] == symbol:
            symbolset.append(reel[i])
            symbolset.append(reel[i+1])
            symbolset.append(reel[i+2])
            allsymbolsets.append(symbolset)
    return allsymbolsets


def checkHowManyLinesWon(reelcase):
    amount_of_lines = 0
    # line1
    if reelcase[0][LINE1[0]] == reelcase[1][LINE1[1]] == reelcase[2][LINE1[2]]:
        amount_of_lines +=1
    # line2
    if reelcase[0][LINE2[0]] == reelcase[1][LINE2[1]] == reelcase[2][LINE2[2]]:
        amount_of_lines +=1
    # line3
    if reelcase[0][LINE3[0]] == reelcase[1][LINE3[1]] == reelcase[2][LINE3[2]]:
        amount_of_lines +=1
    # line4
    if reelcase[0][LINE4[0]] == reelcase[1][LINE4[1]] == reelcase[2][LINE4[2]]:
        amount_of_lines +=1
    # line5
    if reelcase[0][LINE5[0]] == reelcase[1][LINE5[1]] == reelcase[2][LINE5[2]]:
        amount_of_lines +=1

    return amount_of_lines


def getReelCase(matrix1, matrix2, matrix3, matrix4, matrix5, winlines):
    best_move = []
    for reel in matrix1:
        for reel2 in matrix2:
            for reel3 in matrix3:
                for reel4 in matrix4:
                    for reel5 in matrix5:
                        if checkHowManyLinesWon([reel, reel2, reel3, reel4, reel5]) <= winlines:
                            best_move.append(reel)
                            best_move.append(reel2)
                            best_move.append(reel3)
                            best_move.append(reel4)
                            best_move.append(reel5)
                            return best_move
                        else:
                            print "no matches, change amount of winlines"


def anysymbolexcept(exclusionlist):
    updatedlist=[]
    for i in list_of_symbols:
        if i not in exclusionlist:
            updatedlist.append(i)
    return random.choice(updatedlist)



symbol_in_combination = input("Enter the symbol number: ")
times_repeat = input("how many symbols in the winning line: ")
additional_winlines  = input("How many addidional win lines allowed: ")
wlines = 1 + additional_winlines
exc_list = [0,9,10]
exc_list.append(symbol_in_combination)
if times_repeat < 5:
    next_symbol = input("Enter the next symbol in the line: ")
    exc_list.append(next_symbol)

    if times_repeat == 2:
        reel1 = getAllSymbolsFromReel(symbol_in_combination,REEL_SET0[0])
        reel2 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[1])
        reel3 = getAllSymbolsFromReel(next_symbol, REEL_SET0[2])
        reel4 = getAllSymbolsFromReel(anysymbolexcept(exc_list), REEL_SET0[3])
        reel5 = getAllSymbolsFromReel(anysymbolexcept(exc_list), REEL_SET0[4])
        reel_case = getReelCase(reel1, reel2, reel3, reel4, reel5, wlines)
        print gettestcase(reel_case)

    elif times_repeat == 3:
        reel1 = getAllSymbolsFromReel(symbol_in_combination,REEL_SET0[0])
        reel2 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[1])
        reel3 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[2])
        reel4 = getAllSymbolsFromReel(next_symbol, REEL_SET0[3])
        reel5 = getAllSymbolsFromReel(anysymbolexcept(exc_list), REEL_SET0[4])
        reel_case = getReelCase(reel1, reel2, reel3, reel4, reel5, wlines)
        print gettestcase(reel_case)

    elif times_repeat == 4:
        reel1 = getAllSymbolsFromReel(symbol_in_combination,REEL_SET0[0])
        reel2 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[1])
        reel3 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[2])
        reel4 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[3])
        reel5 = getAllSymbolsFromReel(next_symbol, REEL_SET0[4])
        reel_case = getReelCase(reel1, reel2, reel3, reel4, reel5, wlines)
        print gettestcase(reel_case)

elif times_repeat == 5:
    reel1 = getAllSymbolsFromReel(symbol_in_combination,REEL_SET0[0])
    reel2 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[1])
    reel3 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[2])
    reel4 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[3])
    reel5 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[4])
    reel_case = getReelCase(reel1, reel2, reel3, reel4, reel5, wlines)
    print gettestcase(reel_case)




