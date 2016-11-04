import time
import random
import itertools
from first import first


REEL_SET0 = [[8,8,8,3,6,0,4,1,5,3,	0,7,2,1,6,6,0,3,5,2,0,4,2,3,0,10,1,6,6,6,2,5,2,7,7,7,3,0,5,0,8,1,4,3,10,3,5,0],
             [8,8,8,2,4,1,4,1,0,10,	1,4,0,1,7,7,7,1,5,0,4,3,0,5,3,6,6,6,3,2,4,2,3,5,1,10,2,4,1,7,7,7,1,3],
             [8,8,8,2,4,1,2,4,1,5,	0,4,0,1,4,0,1,5,0,6,6,1,4,3,5,0,8,8,8,0,5,2,3,6,6,3,5,2,4,2,3,5,1,0,10,2,4,0,5,1,7,7,7,1,3],
             [8,8,1,2,10,0,5,1,7,7,	0,4,3,0,6,6,2,4,0,5,0,6,6,6,2,5,0,4,1,10,0,4,2,5,3,8,8,8,0,1,4,3,0,7,7,7,3,10,2,1,5,3,4,3,2,5,0],
             [8,8,1,2,10,1,5,1,7,7,	0,4,3,10,1,6,6,2,4,0,5,1,6,6,6,2,5,1,4,1,10,1,4,2,5,3,8,8,8,0,1,4,3,0,7,7,7,2,5,3,4,3,2,5,1]]

REEL_SET1 = [[8,8,8,3,11,2,6,0,4,11,2,5,3,11,0,7,2,11,3,6,6,4,1,5,11,2,0,10,2,5,11,0,1,6,6,6,0,5,1,7,7,7,3,2,5,0,8,1,4,3,10,3,5,0],
             [8,8,8,2,4,1,4,1,0,10,1,4,0,1,7,7,7,1,5,0,4,3,0,5,3,6,6,6,3,2,4,2,3,5,1,10,2,4,1,7,7,7,1,3],
             [8,8,8,2,4,1,11,0,4,1,5,2,4,11,1,4,0,1,5,0,6,6,1,4,3,5,0,8,8,8,0,5,2,11,3,6,6,3,5,2,4,2,11,3,5,1,4,0,10,2,0,0,5,1,7,7,7,1,3],
             [8,8,1,2,10,0,5,1,7,7,0,4,3,0,6,6,2,4,0,5,0,6,6,6,2,5,0,4,1,10,0,4,2,5,3,8,8,8,0,1,4,3,0,7,7,7,3,2,5,3,4,3,2,5,0],
             [8,8,1,2,10,1,5,1,7,7,0,4,3,10,1,6,6,2,11,0,5,1,6,6,6,2,5,1,11,1,1,4,2,5,3,8,8,8,0,1,4,3,0,7,7,7,2,5,3,4,3,11,2,5,1]]

REEL_SET_FreeGames =\
            [[2,3,8,8,8,0,2,5,0,2,3,0,5,2,10,3,5,0,3,5,2,3,5,10,0],
             [4,0,8,8,8,3,1,8,8,8],
             [5,4,8,8,8,2,1,8,8,8],
             [1,4,8,8,8,5,0,8,3,2,8,8],
             [4,2,8,8,8,0,5,8,8,3,1,8]]
ALL_REEL_SETS = [REEL_SET0, REEL_SET1, REEL_SET_FreeGames]



BET = 1

# Symbols:
bar1        = 0
bar2        = 1
bar3        = 2
horse_shoe  = 3
dollar      = 4
gold        = 5
blue7       = 6
green7      = 7
red7        = 8
flame_gem   = 9
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
    bar1         : (0,	0,	0.5,	1,		2.5),
    bar2         : (0,	0,	0.5,	1.5,	5),
    bar3         : (0,	0,	0.5,	2,		7.5),
    horse_shoe   : (0,	0,	1,		3,		10),
    dollar       : (0,	0,	1,		3,		10),
    gold         : (0,	0,	1,		3,		10),
    blue7        : (0,	0,	2,		6,		20),
    green7       : (0,	0,	3,		8,		30),
    red7         : (0,	0,	4,		10,		40),
    flame_gem    : (0,	0,	5,		50,		500),
    WILD         : (0,	0,	5,		50,		500),
}

distr_reels = {
 0 : 0,
 1 : 495,
}


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



def get_symbol_indecies1(reel, symbol):
    """
    :param reel:  list of symbols given in math
    :param symbol: interger that points to needed
    :return: list of indecies on the reel for given symbol
    """
    result = []
    for index in range(len(reel)-2):
        if reel[index] == symbol and reel[index+1] == symbol and reel[index+2]!=symbol:
            result.append(index)
    return result


def get_symbol_indecies2(reel, symbol):
    """
    :param reel:  list of symbols given in math
    :param symbol: interger that points to needed
    :return: list of indecies on the reel for given symbol
    """
    result = []
    for index in range(len(reel)-2):
        if reel[index] == symbol and reel[index+1] == symbol and reel[index+2]==symbol:
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


def check_if_wline(reelset, new_comb, wline):
    """
    :param reelset: list of lists where each list is a reel
    :param new_comb: list of indecies on each reel
    :param wline: list of symbols
    :return: True/False whether wline is there
    """

    for i in range(len(reelset)):
        if reelset[i][new_comb[i]] != wline[i]:
            return False
    return True


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


def get_test_case(reelcase, reelset, fs=False):
    if not fs:
        testcase = [0,]
    else:
        testcase = [495,]
    # testcase.append(get_reelset_index(reelset))
    for i in range(len(reelset)):
        testcase.append(get_comb_index(reelcase[i], reelset[i]))
    return testcase


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


def get_best_reelcase(all_comb, reelset,wline):
    """
    :param all_comb: List of all combinations where needed winning line is present. result of sorted_comb()
    :param wline: list of winnnig symbols
    :return: reelcase with min amount of wining lines
    """
    best_move = []
    winlines = len(LINES)
    for combination in all_comb:
        reelcase = getReelCaseFromComb(reelset, combination)
        lines_won = checkHowManyLinesWon(reelcase)
        if lines_won == 1:
            return reelcase
        if lines_won<=winlines:
            best_move = reelcase
            winlines = lines_won
    return best_move



def compare_Best_moves(reelset, move1, move2):
    """
    :param reelset: list of lists where each inner list is a reel
    :param comb1:
    :param comb2:
    :return: returns combination with smallest amount of wining lines
    """
    lines_won1 = checkHowManyLinesWon(move1)
    lines_won2 = checkHowManyLinesWon(move2)
    if lines_won1>lines_won2:
        return move2
    else:
        return move1


def avarageSymbol_value(reelset, symbol):
    """
    :param reelset: list of lists where each inner list is a reel
    :param symbol: integer that represents a symbol on the reel
    :return: avarage value of given symbol for a reel from given reelset
    """
    z = len(reelset)
    all_symbol = 0.0
    for i in range(z):
        for j in range(len(reelset[i])):
            if reelset[i][j] == symbol:
                all_symbol += 1
    return all_symbol/z


def append_non_win_reel(win_move,reelset):
    """
    :param win_move: list of lists where each inner list contains a reel symbols
    :param reelset: list of lists where each inner list is a reel
    :return: adds 1 more reel to the reelcase without increasing amount of wining lines
    """
    next_reel_index = len(win_move)
    for i in range(len(reelset[next_reel_index])):
        possible_reelview = reelset[next_reel_index][i:i+3]
        equal = False
        for symbol in win_move[next_reel_index-1]:
            for pos_symbol in possible_reelview:
                if symbol == pos_symbol or pos_symbol == WILD:
                    equal = True
        if equal == False:
            win_move.append(possible_reelview)
            break
    return win_move


def get_fs_test_case(reelset):
    """
    :param reelset: list of lists where each inner list is a reel
    :return: test case
    """
    # switch_witches = (1,2,3)
    test_case = []
    reelview = []

    # create reelcase which will give you the bonus
    for i in range(len(reelset[0])):
        if reelset[0][i] == SCATTER:
            first_reel_view = reelset[0][i:i+3]
            reelview.append(first_reel_view)
            break
    reelview =  append_non_win_reel(reelview,reelset)
    for j in range(len(reelset[2])):
        if reelset[2][j] == SCATTER:
            third_reel_view = reelset[2][j:j+3]
            reelview.append(third_reel_view)
            break
    reelview = append_non_win_reel(reelview, reelset)
    for z in range(len(reelset[4])):
        if reelset[4][z] == SCATTER:
            last_reel_view = reelset[4][z:z + 3]
            reelview.append(last_reel_view)
            break
    # add part for FS
    test_case = get_test_case(reelview,reelset, fs=True)
    test_case.append(5) # no boost win

    return test_case


def script_loop(reelset, symbol, times_repeat, nextsymbol=None):
    """
    :param reelset: list of lists where each inner list is a reel
    :param symbol: what symbol you want to get in winline
    :param times_repeat: how many winning symbols in combination
    :param nextsymbol: what symbol should be next after your combination
    :returns tuple -(testcase, best_move)
    """
    wline = []
    for i in range(times_repeat):
        wline.append(symbol)
    if nextsymbol != None:
        wline.append(nextsymbol)
    comb_list = []
    for i in range(len(wline)):
        reel_comb = get_symbol_indecies(reelset[i],wline[i])
        comb_list.append(reel_comb)
    product_comb = itertools.product(*comb_list)
    sorted_product = sorted_comb(product_comb,reelset[0:len(wline)],wline)
    best_move      = get_best_reelcase(sorted_product,reelset[0:len(wline)], wline)
    if len(best_move) < len(reelset):
        best_move      = append_non_win_reel(best_move,reelset)
    test_case      = get_test_case(best_move, reelset)
    return  test_case, best_move


def script_loop_big_symbol(reelset, symbol, times_repeat, nextsymbol=None,big7=2):
    """
    :param reelset: list of lists where each inner list is a reel
    :param symbol: what symbol you want to get in winline
    :param times_repeat: how many winning symbols in combination
    :param nextsymbol: what symbol should be next after your combination
    :returns tuple -(testcase, best_move)
    """
    wline = []
    for i in range(times_repeat):
        wline.append(symbol)
    if nextsymbol != None:
        wline.append(nextsymbol)
    comb_list = []
    for i in range(len(wline)):
        if big7=='2':
            reel_comb = get_symbol_indecies2(reelset[i],wline[i])
            comb_list.append(reel_comb)
        elif big7=='1':
            reel_comb = get_symbol_indecies1(reelset[i], wline[i])
            comb_list.append(reel_comb)
    product_comb = itertools.product(*comb_list)
    for comb in product_comb:
        f_move = comb
        break
    best_move = getReelCaseFromComb(reelset, f_move)
    if len(best_move) < len(reelset):
        best_move      = append_non_win_reel(best_move,reelset)
    test_case      = get_test_case(best_move, reelset)
    return  test_case, best_move


def console_test_case(test_case_name, test_case):
    """
    :param test_case_name: name for the test case
    :param test_case: list of reel indecies
    :return:  prints the modified test case to console
    """
    part1 = '"%s"' % test_case_name
    part2 = ": {\n        data: %s;\n    };" % test_case
    print part1+part2
    print "-"*30


def console_payout(bet, best_move):
    """
    :param bet: bet amount
    :param best_move: list of lists where each inner list is consist of reel symbols
    :return: prints payout to the console
    """
    payout = calculate_payout(bet,best_move)
    print "Payout: %s" % payout
    print "-"*30




test_case_name = raw_input("Enter the name for the testcase: ")
FS             = raw_input("Do you need FS test case? Yes/No: ")
big7           = raw_input("Do you need big 7 b3 test case? 0/1/2: ")

if FS == "y" or FS=="Yes" or FS=='yes':
    start_time = time.time()
    test_case = get_fs_test_case(REEL_SET1)
    console_test_case(test_case_name, test_case)

elif big7>0:
    symbol_in_combination = input("Enter the symbol number: ")
    times_repeat = input("how many symbols in the winning line: ")
    if times_repeat < 5:
        next_symbol = input("Enter the next symbol in the line(type 99 if it doesn't matter): ")
        if next_symbol == 99:
            next_symbol = random.randrange(1, 9)
    else:
        next_symbol = None
    start_time = time.time()
    script_loop = script_loop_big_symbol(REEL_SET_FreeGames, symbol_in_combination, times_repeat, next_symbol, big7)
    test_case = script_loop[0]
    best_move = script_loop[1]
    console_test_case(test_case_name, test_case)
    console_payout(BET, best_move)
else:
    symbol_in_combination = input("Enter the symbol number: ")
    times_repeat          = input("how many symbols in the winning line: ")
    if times_repeat < 5:
        next_symbol = input("Enter the next symbol in the line(type 99 if it doesn't matter): ")
        if next_symbol == 99:
            next_symbol = random.randrange(1,9)
    else:
        next_symbol = None
    start_time = time.time()
    test_case = script_loop(REEL_SET0, symbol_in_combination,times_repeat,next_symbol)[0]
    best_move = script_loop(REEL_SET0, symbol_in_combination,times_repeat,next_symbol)[1]
    console_test_case(test_case_name, test_case)
    console_payout(BET,best_move)
print("--- %s seconds ---" % (time.time() - start_time))
