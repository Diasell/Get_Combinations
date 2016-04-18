import time
import random
import itertools
from first import first


REEL_SET0 = [[1,7,8,0,5,8,7,2,4,9,2, 5,8,1,2,4,5,3,0,6,5, 4,8,10,1,6,7,1,6,2,4,5,3,1,8,6,3,4,1,0, 5,4,8,3,1,5,3,6,8,10,0,4,1,2,3,1,7,2,1,4, 0,6,5,4,7,3,0,2,7,1,3,5,4,2,10,1,3,2,7,4, 3,8,4,3,6,2,3,4,5,6, 2,1,5,3,7,2,5,1,7,3,9,5,2,4,1,3,2,1,6,7,2,1,8,4,6,0,3,7,1,3,2,6,1,2,10,5,4,2,6],
             [3,1,0,8,2,0,3,6,2,7,4, 2,1,4,3,1,5,3,2,4,5, 6,7,0,1,4,0,7,2,1,5, 8,1,6,2,3,6,5,1,8,5, 2,6,1,2,7,1,5,7,2,4, 1,5,6,2,5,7,4,1,2,7, 3,2,1,8,2,1,3,5,4,9, 5,4,3,8,4,3,9,1,7,3, 1,0,5,1,3,6,5,1,4,8, 1,3,6,2,7,4,0,6,4,2, 6,7,1,2,4,6,3,9,2,3, 7,6,3,4,2,5,1,2,3,8,5,3,4,8,3,4,2],
             [4,6,1,2,5,4,6,3,4,1,3, 7,6,4,2,6,1,3,8,5,2, 4,6,1,7,4,2,1,3,2,5, 7,2,6,7,8,3,1,4,9,8, 0,3,1,8,4,5,2,6,8,5, 0,6,3,7,1,2,4,0,6,3, 1,2,4,3,7,0,3,1,5,9, 4,3,2,1,5,0,1,5,3,4, 1,2,5,1,2,3,8,2,5,4, 3,0,9,7,1,4,7,2,4,5, 8,1,3,7,2,1,7,6,5,2, 6,1,3,6,5,2,3,1,2,8,1,2,5,4,3,7,2],
             [3,6,9,8,4,3,6,4,2,6,0, 2,7,3,2,8,1,0,6,4,2, 5,7,1,2,7,3,1,9,8,2, 7,4,2,5,7,8,3,5,2,8, 3,0,2,7,4,1,2,6,1,5, 9,0,6,1,4,5,1,2,6,3, 4,1,0,5,6,8,4,5,1,2, 0,3,5,2,1,3,6,7,3,1, 4,2,5,7,1,3,4,1,3,2, 4,1,5,4,1,3,2,8,6,5, 1,6,7,1,8,6,1,5,3,2, 4,3,2,7,1,3,4,7,3,5,1,3,2,4,1,2,4],
             [3,1,6,7,1,6,7,2,5,1,3, 7,6,8,5,6,1,2,5,4,10, 1,5,7,6,0,5,6,4,1,3, 8,0,3,4,1,3,5,0,4,2, 5,3,7,2,4,3,8,1,7,6, 1,9,4,5,2,8,4,2,7,3, 4,10,2,1,3,2,5,9,1,4, 0,2,1,3,2,4,6,1,5,0, 2,1,3,10,1,4,2,6,3,0, 2,5,6,9,2,4,5,3,2,1, 8,3,2,1,3,2,8,3,2,1, 7,4,8,2,1,4,3,10,1,2, 4,8,5,3,1,6,7,4]]

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
         LINE12,LINE13,LINE14,LINE15,LINE16,LINE17,LINE18,LINE19,LINE20]


list_of_symbols = range(11)
x2_symbols = [9,8,7,6,5]


# Symbols:
SCATTER     = 0
AMULET      = 1
POISON      = 2
SCULL       = 3
CROW        = 4
CAT         = 5
GREEN_WITCH = 6
RED_WITCH   = 7
BLUE_WITCH  = 8
WILD        = 9
BONUS       = 10

symbols_names = {
    SCATTER     : "SCATTER",
    AMULET      : "AMULET",
    POISON      : "POISON",
    SCULL       : "SCULL",
    CROW        : "CROW",
    CAT         : "CAT",
    GREEN_WITCH : "GREEN_WITCH",
    RED_WITCH   : "RED_WITCH",
    BLUE_WITCH  : "BLUE_WITCH",
    WILD        : "WILD"
}


paytable = {
    WILD        : (0, 0.2, 2, 5, 10),
    GREEN_WITCH : (0, 0.2, 2, 5, 10),
    BLUE_WITCH  : (0, 0.2, 2, 5, 10),
    RED_WITCH   : (0, 0.2, 2, 5, 10),
    CAT         : (0, 0.2, 1.5, 4, 7),
    SCULL       : (0, 0, 0.2, 2, 2.5),
    CROW        : (0, 0, 0.2, 2, 2.5),
    AMULET      : (0, 0, 0.2, 1, 1.5),
    POISON      : (0, 0, 0.2, 1, 1.5),
    SCATTER     : (0, 0, 2, 5, 10)
}

def first_win_symbol_inline(symbol):
    """
    gives you info about how much min symbols needed to get win
    """
    for i in range(len(paytable[symbol]), 0, -1):
        if paytable[symbol][i - 1] == 0:
            min_needed_symbols = i + 1
            break
    return min_needed_symbols

def get_all_symbol_combination(list_of_symbols):
    """
    :returns all combination for all given symbols as a
     list of dictionaries where each dict looks like {"2xSymbol_name": [symbol,...x]}
    """
    result = []
    for symbol in list_of_symbols:
        for i in range(first_win_symbol_inline(symbol), 6,1):
            symbol_combination = {}
            case = []
            comb_name = str(i) + "x" + symbols_names[symbol]
            for j in range(i):
                case.append(symbol)
            while len(case) < 5:
                next_symbol = random.choice(list_of_symbols)
                if next_symbol != WILD and next_symbol != symbol and next_symbol!= BONUS:
                    case.append(next_symbol)
            symbol_combination[comb_name] = case
            result.append(symbol_combination)
    return  result




def get_symbol_indecies(reel, symbol):
    """
    :param reel:  list of symbols given in math
    :param symbol: interger that points to needed
    :return: list of indecies on the reel for given symbol
    """
    result = []
    for index in range(len(reel)):
        if reel[index] == symbol:
            result.append(index)
    return result


def get_line_combination(combination, line):
    """
    :param combination: list of indecies on each reel
    :param line:  list of
    :return:  list of indecies for
    """
    new_combination = []
    for i in range(len(combination)):
        new_index = combination[i] - line[i]
        new_combination.append(new_index)
    return new_combination



def sorted_comb(all_comb, reelset, wline):
    """
    :param all_comb: list of tuples. Where tuple is a 5 indecies each for each reel
    :param reelset: list of lists where each list is a reel
    :param wline: list of symbols
    :return: List of all combinations where needed winning line is present
    """

    for comb in all_comb:
        for line in LINES:
             yield  get_line_combination(comb,line)


def getReelCaseFromComb(reelset, combination):
    """
    :param reelset: list of lists where each list is a reel
    :param combination: list of indecies on each reel
    :return: list of lists where each inner list consist of 3 symbols
    """
    reelcase = []
    for i in range(len(reelset)):
        reel = reelset[i]
        full_reel =reel + reel[0:5]
        if combination[i]>=0:
            reelview = full_reel[combination[i]:combination[i]+3]
        else:
            y = combination[i] + len(reel)
            reelview = full_reel[y:y+3]
        reelcase.append(reelview)
    return reelcase


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
    test = [reel[i] for reel, i in itertools.izip(reelcase, line)]

    return test


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
    return len(list(itertools.takewhile(lambda symbol: symbol == first_symbol, lst)))


def get_reelcase_by_line(all_comb, reelset, wline, given_line):
    """
    :param all_comb: List of all combinations where needed winning line is present. result of sorted_comb()
    :param wline: list of winnnig symbols
    :return: reelcase with min amount of wining lines
    """
    for combination in all_comb:
        reelcase = getReelCaseFromComb(reelset, combination)
        if ifwinline(given_line,reelcase):
            return reelcase


def main_loop(reelset, dict_case, given_line ):
    """
    :param reelset: list of lists where each inner list is a reel
    :param dict_case: dict that looks like {"testcasename": testcase value}
    :param given_line: line that you want to see win combination on
    :prints out the tag with test case to console
    """

    name = dict_case.keys()[0]
    wline = dict_case.values()[0]
    comb_list = []
    for i in range(len(wline)):
        reel_comb = get_symbol_indecies(reelset[i],wline[i])
        comb_list.append(reel_comb)

    product_comb   = itertools.product(*comb_list)
    sorted_product = sorted_comb(product_comb,reelset[0:len(wline)],wline)
    best_move      = get_reelcase_by_line(sorted_product,reelset[0:len(wline)], wline, given_line)
    test_case      = get_test_case(best_move, reelset)
    console_test_case(test_case,name)


def console_test_case(test_case, name):
    """
    """
    str_case = '<random name="%s" values="%d, %d,%d,%d,%d,%d"/>' % (name, test_case[0],
                                                                    test_case[1],
                                                                    test_case[2],
                                                                    test_case[3],
                                                                    test_case[4],
                                                                    test_case[5])
    print str_case + '\n'



input_line = input("Win line number: ")
given_line = LINES[input_line-1]


all_comb = get_all_symbol_combination(range(10))

for combination in all_comb:
    main_loop(REEL_SET0, combination, given_line)