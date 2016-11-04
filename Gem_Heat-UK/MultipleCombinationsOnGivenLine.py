import time
import random
import itertools
from first import first


REEL_SET0 = [[8,8,8,3,6,0,4,1,5,3,	0,7,2,1,6,6,0,3,5,2,0,4,2,3,0,10,1,6,6,6,2,5,2,7,7,7,3,0,5,0,8,1,4,3,10,3,5,0],
             [8,8,8,2,4,1,4,1,0,10,	1,4,0,1,7,7,7,1,5,0,4,3,0,5,3,6,6,6,3,2,4,2,3,5,1,10,2,4,1,7,7,7,1,3],
             [8,8,8,2,4,1,2,4,1,5,	0,4,0,1,4,0,1,5,0,6,6,1,4,3,5,0,8,8,8,0,5,2,3,6,6,3,5,2,4,2,3,5,1,0,10,2,4,0,5,1,7,7,7,1,3],
             [8,8,1,2,10,0,5,1,7,7,	0,4,3,0,6,6,2,4,0,5,0,6,6,6,2,5,0,4,1,10,0,4,2,5,3,8,8,8,0,1,4,3,0,7,7,7,3,10,2,1,5,3,4,3,2,5,0],
             [8,8,1,2,10,1,5,1,7,7,	0,4,3,10,1,6,6,2,4,0,5,1,6,6,6,2,5,1,4,1,10,1,4,2,5,3,8,8,8,0,1,4,3,0,7,7,7,2,5,3,4,3,2,5,1]]

REEL_SET_FreeGames =\
            [[2,3,8,8,8,0,2,5,0,2,3,0,5,2,10,3,5,0,3,5,2,3,5,10,0],
             [4,0,8,8,8,3,1,8,8,8],
             [5,4,8,8,8,2,1,8,8,8],
             [1,4,8,8,8,5,0,8,3,2,8,8],
             [4,2,8,8,8,0,5,8,8,3,1,8]]
ALL_REEL_SETS = [REEL_SET0, REEL_SET_FreeGames]


BET = 1

# Symbols:
BAR1        = 0
BAR2        = 1
BAR3        = 2
HORSE_SHOE  = 3
DOLLAR      = 4
GOLD        = 5
BLUE7       = 6
GREEN7      = 7
RED7        = 8
FLAME_GEM   = 9
WILD        = 10
SCATTER     = 11


list_of_symbols = range(12)
x2_symbols = []

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
LINE10 = [1,1,2,1,1]

LINES = [LINE1,LINE2,LINE3,LINE4,LINE5,LINE6,LINE7,LINE8,LINE9,LINE10]


paytable = {
    BAR1         : (0,	0,	0.5,	1,		2.5),
    BAR2         : (0,	0,	0.5,	1.5,	5),
    BAR3         : (0,	0,	0.5,	2,		7.5),
    HORSE_SHOE   : (0,	0,	1,		3,		10),
    DOLLAR       : (0,	0,	1,		3,		10),
    GOLD         : (0,	0,	1,		3,		10),
    BLUE7        : (0,	0,	2,		6,		20),
    GREEN7       : (0,	0,	3,		8,		30),
    RED7         : (0,	0,	4,		10,		40),
    FLAME_GEM    : (0,	0,	5,		50,		500),
    WILD         : (0,	0,	5,		50,		500),
}

symbols_names = {
    RED7        : "RED 7",
    GREEN7      : "GREEN 7",
    BLUE7       : "BLUE 7",
    BAR1        : "BARx1",
    BAR2        : "BARx2",
    BAR3        : "BARx3",
    HORSE_SHOE  : "HORSE SHOE",
    DOLLAR      : "DOLLAR",
    WILD        : "WILD",
    GOLD        : "GOLD",
    FLAME_GEM   : "FLAME GEM"
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

def get_all_symbol_combination(list_of_symbols, reelset):
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
                next_symbol = random.choice(reelset[len(case)])
                if next_symbol != WILD and next_symbol != symbol:
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



def ifwinline(line, wline, reelcase):
    """
    Checks if the line is a winning one
    """
    list_of_line_symbols = lineview(line, reelcase)
    first_symbol = firstinline(list_of_line_symbols)
    q_win_symbols = get_amount_of_win_symbols(list_of_line_symbols, first_symbol)
    q_win_symbols_wline = get_amount_of_win_symbols(wline, first_symbol)
    if q_win_symbols == q_win_symbols_wline:
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
        if ifwinline(given_line,wline,reelcase):
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
    str_case = '"%s": {\n    data:[%d, %d,%d,%d,%d,%d];\n};' % (name, test_case[0],
                                                                    test_case[1],
                                                                    test_case[2],
                                                                    test_case[3],
                                                                    test_case[4],
                                                                    test_case[5])
    print str_case + '\n'



input_line = input("Win line number: ")
given_line = LINES[input_line-1]


all_comb = get_all_symbol_combination([BAR1,BAR2,BAR3,HORSE_SHOE,DOLLAR,GOLD,BLUE7,GREEN7,RED7,WILD], REEL_SET0)

for combination in all_comb:
    main_loop(REEL_SET0, combination, given_line)