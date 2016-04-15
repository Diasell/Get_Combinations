import time
import random
import itertools
from first import first


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


BET = 1

# Symbols:
SCATTER     = 0
AMULET      = 1
POISON      = 2
SKULL       = 3
CROW        = 4
CAT         = 5
GREEN_WITCH = 6
RED_WITCH   = 7
BLUE_WITCH  = 8
WILD        = 9
BONUS       = 10

list_of_symbols = range(11)
x2_symbols = [9,8,7,6,5]

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


paytable = {
    WILD        : [0, 0.2, 2, 5, 10],
    GREEN_WITCH : (0, 0.2, 2, 5, 10),
    BLUE_WITCH  : (0, 0.2, 2, 5, 10),
    RED_WITCH   : (0, 0.2, 2, 5, 10),
    CAT         : (0, 0.2, 1.5, 4, 7),
    SKULL       : (0, 0, 0.2, 2, 2.5),
    CROW        : (0, 0, 0.2, 2, 2.5),
    AMULET      : (0, 0, 0.2, 1, 1.5),
    POISON      : (0, 0, 0.2, 1, 1.5),
    SCATTER     : (0, 0, 2, 5, 10)
}


def get_reelset_index(reelset):
    """
    :param reelset: REEL_SET
    :return: index of the given reelset in ALL_REEL_SETS list
    """
    for i in range(len(ALL_REEL_SETS)):
        if ALL_REEL_SETS[i] == reelset:
            return i

def get_comb_index(comb, reel):
    """
    :param comb: visible to a player part of the reel(basically element of reelcase)
    :param reel: part of REEL_SET where you want to look for comination
    :return: index of the 1st element of the combination
    """
    full_reel = list(itertools.chain(reel, reel[0:2]))
    for i in range(len(reel)):
        if full_reel[i] == comb[0] and full_reel[i+1] == comb[1] and full_reel[i+2] == comb[2]:
            return i


def get_test_case(reelcase, reelset):
    testcase = []
    testcase.append(get_reelset_index(reelset))
    for i in range(len(reelset)):
        testcase.append(get_comb_index(reelcase[i], reelset[i]))
    return testcase



def getAllSymbolsFromReel(symbol, reel):
    """
    :param symbol: symbol that you want to get a combination with
    :param reel: whole reel sub list of REEL_SET
    :return: list of lists with all combinations of reels with your symbol
    """
    full_reel = list(itertools.chain(reel, reel[0:3]))
    allsymbolsets = []
    for i in range(len(reel)):
        if reel[i] == symbol:
            sym_range1 = reel[i-2:i] + full_reel[i:i+1]
            sym_range2 = reel[i-1:i]+ full_reel[i:i+2]
            sym_range3 = full_reel[i:i+3]
            allsymbolsets.append(sym_range1)
            allsymbolsets.append(sym_range2)
            allsymbolsets.append(sym_range3)
    allsymbolsets.sort()
    return list(i for i,_ in itertools.groupby(allsymbolsets))


def checkHowManyLinesWon(reelcase):
    """
    Checks how many line won on the given reelcase
    """
    amount_of_lines = 0
    for line in LINES:
        if ifwinline(line,reelcase):
            amount_of_lines +=1
    return amount_of_lines


def ifwinline(line, reelcase):
    """
    Checks if the line is a winning one
    """
    list_of_line_symbols = lineview(line, reelcase)
    first_symbol = firstinline(list_of_line_symbols)
    q_win_symbols = get_amount_of_win_symbols(list_of_line_symbols, first_symbol)
    if first_symbol in x2_symbols and q_win_symbols==2:
        return True
    elif q_win_symbols>=3:
        return True
    else:
        return False



def lineview(line, reelcase):
    """
    :param line:  list of indexes  which will give you needed element of the reel
    :param reelcase: list of reels
    :return: list of symbols on given line
    """
    return [reel[i] for reel, i in itertools.izip(reelcase, line)]


def firstinline(iterable):
    """
    :param iterable: list of line symbols
    :return: first element of win combintation
    """
    return first(iterable, WILD, key=lambda symbol: symbol != WILD)

def get_amount_of_win_symbols(lst, first_symbol):
    """
    :param lst: list of symobls in the line
    :param first_symbol: first symbol of the line combination
    :return: the quantity of winning symbols in the line
    """
    return len(list(itertools.takewhile(lambda symbol: symbol == first_symbol or symbol==WILD, lst)))



def linepayout(bet,line,reelcase):
    """
    Returns how much should be paid for this winning line
    """
    list_of_line_symbols = lineview(line, reelcase)
    first_symbol = firstinline(list_of_line_symbols)
    q_win_symbols = get_amount_of_win_symbols(list_of_line_symbols, first_symbol)
    return bet * paytable[first_symbol][q_win_symbols-1]

def scatterpayout(bet, reelcase):
    """
    :param bet:  playets bet
    :param reelcase: set of reels that users see on the screen
    :return: payout for scatters on the reelcase
    """
    scatters_count = 0
    for i in range(5):
        for j in range(3):
            if reelcase[i][j] == SCATTER:
                scatters_count+=1
    if scatters_count == 0:
        return 0
    else:
        return bet * paytable[SCATTER][scatters_count-1]


def calculate_payout(bet, reelcase):
    """
    :param bet: playets bet
    :param reelcase: set of reels that users see on the screen
    :return: total payout
    """
    payout_for_lines = 0
    for line in LINES:
        payout_for_lines += linepayout(bet, line, reelcase)
    return scatterpayout(bet, reelcase) + payout_for_lines



def line_is_there(reelcase, wline):
    """
    :param reelcase: set of reels that users see on the screen
    :param wline: its a list that consist of symbols for each reel
    :return: True\False whether this line is present as a win line in this reelcase
    """
    for line in LINES:
        if lineview(line,reelcase) == wline:
            return True
    return False


"""
def getReelCase(matrix1, matrix2, matrix3, matrix4, matrix5, wline):

    :param matrix1: list of lists of possible combinations on reel 1
    :param matrix2: list of lists of possible combinations on reel 2
    :param matrix3: list of lists of possible combinations on reel 3
    :param matrix4: list of lists of possible combinations on reel 4
    :param matrix5: list of lists of possible combinations on reel 5
    :param wline: list of symbols that should be present on the reelcase as a winline
    :return: a list that contains the coordinates of best position on each reel which gives a min amount of winlines

    best_move = []
    min_lines = 20
    for reel1 in matrix1:
        for reel2 in matrix2:
            for reel3 in matrix3:
                for reel4 in matrix4:
                    for reel5 in matrix5:
                        reelcase = [reel1, reel2, reel3, reel4, reel5]
                        if line_is_there(reelcase,wline):
                            if checkHowManyLinesWon(reelcase) <= min_lines:
                                best_move = reelcase
                                min_lines = checkHowManyLinesWon(reelcase)
    return best_move
"""
def getReelCase(matrix1, matrix2, matrix3, matrix4, matrix5, wline):
    """
    :param matrix1: list of lists of possible combinations on reel 1
    :param matrix2: list of lists of possible combinations on reel 2
    :param matrix3: list of lists of possible combinations on reel 3
    :param matrix4: list of lists of possible combinations on reel 4
    :param matrix5: list of lists of possible combinations on reel 5
    :param wline: list of symbols that should be present on the reelcase as a winline
    :return: a list that contains the coordinates of best position on each reel which gives a min amount of winlines
    """
    all_combinations = itertools.product(matrix1,matrix2,matrix3,matrix4,matrix5)
    all_comb_with_wline = itertools.ifilter(lambda x: line_is_there(x,wline), all_combinations)
    min_lines=20
    best_move = []
    for reelcase in all_comb_with_wline:
        if checkHowManyLinesWon(reelcase) <= min_lines:
            best_move = reelcase
            min_lines = checkHowManyLinesWon(reelcase)

    return best_move

def anysymbolexcept(exclusionlist):
    updatedlist=[]
    for i in list_of_symbols:
        if i not in exclusionlist:
            updatedlist.append(i)
    return random.choice(updatedlist)


test_case_name        = raw_input("Enter the name for the testcase: ")
symbol_in_combination = input("Enter the symbol number: ")
times_repeat          = input("how many symbols in the winning line: ")

start_time = time.time()

exc_list = [0,9,10]
exc_list.append(symbol_in_combination)


if times_repeat < 5:
    next_symbol = input("Enter the next symbol in the line(type 99 if it doesn't matter): ")
    if next_symbol == 99:
        next_symbol = random.randrange(1,9)
    exc_list.append(next_symbol)

    if times_repeat == 2:
        s4 = anysymbolexcept(exc_list)
        s5 = anysymbolexcept(exc_list)
        reel1 = getAllSymbolsFromReel(symbol_in_combination,REEL_SET0[0])
        reel2 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[1])
        reel3 = getAllSymbolsFromReel(next_symbol, REEL_SET0[2])
        reel4 = getAllSymbolsFromReel(s4, REEL_SET0[3])
        reel5 = getAllSymbolsFromReel(s5, REEL_SET0[4])
        wline = [symbol_in_combination,symbol_in_combination,next_symbol,s4,s5]
        reel_case = getReelCase(reel1, reel2, reel3, reel4, reel5, wline)
        test_case = get_test_case(reel_case, REEL_SET0)

    elif times_repeat == 3:
        s5 = anysymbolexcept(exc_list)
        reel1 = getAllSymbolsFromReel(symbol_in_combination,REEL_SET0[0])
        reel2 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[1])
        reel3 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[2])
        reel4 = getAllSymbolsFromReel(next_symbol, REEL_SET0[3])
        reel5 = getAllSymbolsFromReel(s5, REEL_SET0[4])
        wline = [symbol_in_combination,symbol_in_combination,symbol_in_combination,next_symbol,s5]
        reel_case = getReelCase(reel1, reel2, reel3, reel4, reel5, wline)
        test_case = get_test_case(reel_case, REEL_SET0)

    elif times_repeat == 4:
        reel1 = getAllSymbolsFromReel(symbol_in_combination,REEL_SET0[0])
        reel2 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[1])
        reel3 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[2])
        reel4 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[3])
        reel5 = getAllSymbolsFromReel(next_symbol, REEL_SET0[4])
        wline = [symbol_in_combination,symbol_in_combination,symbol_in_combination,symbol_in_combination,next_symbol]
        reel_case = getReelCase(reel1, reel2, reel3, reel4, reel5, wline)
        test_case = get_test_case(reel_case, REEL_SET0)

elif times_repeat == 5:
    reel1 = getAllSymbolsFromReel(symbol_in_combination,REEL_SET0[0])
    reel2 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[1])
    reel3 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[2])
    reel4 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[3])
    reel5 = getAllSymbolsFromReel(symbol_in_combination, REEL_SET0[4])
    wline= [symbol_in_combination,symbol_in_combination,symbol_in_combination,symbol_in_combination,symbol_in_combination]
    reel_case = getReelCase(reel1, reel2, reel3, reel4, reel5, wline)
    test_case = get_test_case(reel_case, REEL_SET0)

payout = calculate_payout(BET,reel_case)
part1 = '"%s"' % test_case_name
part2 = ": {\n        data: %s;\n    };" % test_case
print part1+part2
print "-"*20
print "Payout: %s" % payout
print("--- %s seconds ---" % (time.time() - start_time))


