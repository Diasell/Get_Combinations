import time
import random
import itertools
from first import first


REEL_SET0 = [[4,10,1,9,7,4,8,3,10,2,	7,5,8,3,10,4,6,3,7,5,	6,11,12,9,10,5,11,1,9,3,	11,2,6,5,8,12,11,4,10,11],
             [6,1,9,3,7,4,8,5,10,7,	2,9,8,3,10,5,6,0,7,5,	6,11,12,8,9,5,11,7,9,3,		8,2,6,4,8,0,11,4,10,9],
             [1,10,9,0,7,4,8,11,10,3,	7,9,8,4,10,11,6,0,7,5,	6,11,12,9,10,5,6,7,2,8,		11,3,6,9,8,0,11,4,8,9],
             [6,1,10,9,7,4,8,11,10,3,	7,9,8,5,10,2,6,3,7,5,	6,11,12,9,6,5,11,7,0,8,		11,3,6,7,8,0,11,4,10,9],
             [6,1,9,3,7,4,8,3,10,7,	2,9,8,3,10,2,6,4,7,5,	6,11,12,9,5,10,4,7,5,8,		11,3,6,5,8,1,11,4,9,2]]

REEL_SET_FreeGames =\
            [[1,7,9,5,10,8,4,11,7,2,	9,6,3,10,8,5,6,8,4,11,		7,3,6,11,5,10,11,1,9,8,		3,11,4,7,10,12,8,2,10,9],
             [1,6,10,4,7,9,5,11,2,7,	0,11,8,3,10,11,0,7,10,5,	6,10,5,8,12,7,3,9,4,8,		11,3,6,8,5,9,11,4,10,9],
             [1,6,10,4,7,9,2,11,7,3,	9,8,0,10,3,6,7,2,10,5,		6,11,12,9,10,5,11,7,2,8,	11,3,6,4,8,0,11,4,10,9],
             [1,9,7,4,10,2,8,11,4,7,	9,2,8,10,3,6,7,0,10,6,		5,11,8,1,9,5,11,9,12,8,		11,3,6,5,9,0,11,4,10,8],
             [1,6,10,4,9,7,2,11,8,1,	9,10,5,11,8,3,10,6,5,10,	11,4,6,9,5,10,11,12,7,8,	3,11,6,2,8,7,11,5,10,9]]



BET = 1

# Symbols:
WILD        = 0
Commodus    = 1
Lucilla     = 2
Gracchus    = 3
Proximo     = 4
Juba        = 5
A           = 6
K           = 7
Q           = 8
J           = 9
TEN         = 10
NINE        = 11
SCATTER     = 12

list_of_symbols = range(13)
x2_symbols = [0,1,2,12]

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

#LINES = [LINE1,LINE2,LINE3,LINE4,LINE5,LINE6,LINE7,LINE8,LINE9,LINE10,LINE11,
         #LINE12,LINE13,LINE14,LINE15,LINE16,LINE17,LINE18,LINE19,LINE20]

LINES = [LINE1,LINE2,LINE3,LINE4,LINE5,LINE6,LINE7,LINE8,LINE9]




paytable = {
    WILD        : (0, 0, 0, 0, 0),
    Commodus    : (0, 8, 75, 500, 5000),
    Lucilla     : (0, 7, 50, 250, 1000),
    Gracchus    : (0, 0, 25, 75, 350),
    Proximo     : (0, 0, 20, 60, 250),
    Juba        : (0, 0, 20, 60, 250),
    A           : (0, 0, 15, 50, 200),
    K           : (0, 0, 15, 50, 200),
    Q           : (0, 0, 10, 40, 120),
    J           : (0, 0, 10, 40, 120),
    TEN         : (0, 0,  8, 20,  75),
    NINE        : (0, 0,  8, 20,  75),
    SCATTER     : (0, 1, 4, 20, 100),
    "257"         : (0, 8, 75, 500, 5000),
    "258"        : (0, 7, 50, 250, 1000),
    "259"         : (0, 0, 25, 75, 350),
    "260"         : (0, 0, 20, 60, 250),
    "261"         : (0, 0, 20, 60, 250),
}


distr_MP = {
    2: 40,
    3: 70,
    4: 80,
    5: 100,
    7: 100,
    10: 50
}

distr_FS = {
 5 : 70,
 7 : 120,
 10: 120,
 20: 80
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


def get_test_case(reelcase, reelset):
    testcase = []
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
    :return: adds more reels to the reelcase without increasing amount of wining lines
    """
    while len(win_move)<len(reelset):
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


def getFSamountWager(FS):
    """
    :param FS: amount of FS that you want to get
    :return: wager that need to be pasted to testcase in order to get needed amount of FS
    """

    if   FS == 5:
        return distr_FS[5]-1
    elif FS ==7:
        return distr_FS[5]
    elif FS == 10:
        return  distr_FS[7] + distr_FS[5]
    elif FS ==20:
        return distr_FS[10] + distr_FS[7] + distr_FS[5]


def getMultiplierWager(MP):
    """
    :param MP: size of MP that you want to get
    :return: wager that need to be pasted to testcase in order to get needed size of MP
    """

    if   MP == 2:
        return distr_MP[2]-1
    elif MP == 3:
        return distr_MP[2]
    elif MP == 4:
        return distr_MP[2] + distr_MP[3]
    elif MP == 5:
        return  distr_MP[4] + distr_MP[2] + distr_MP[3]
    elif MP == 7:
        return distr_MP[5]+ distr_MP[4] + distr_MP[2] + distr_MP[3]
    elif MP == 10:
        return distr_MP[7] + distr_MP[5] + distr_MP[4] + distr_MP[2] + distr_MP[3]


def get_bonus_test_case(reelset,FS,MP):
    """
    :param reelset: list of lists where each inner list is a reel
    :param FS: amount of free spins (choose from existing variants)
    :param MP: size of multiplier (choose from existing variants)
    :param win_no_win: True by default but  you can change it to False so you will win nothing during the bonus
    :return: test case
    """
    switch_witches = (1,2,3)
    test_case = []
    first_reel_view = []
    last_reel_view  = []

    # create reelcase which will give you the bonus
    for i in range(len(reelset[0])):
        if reelset[0][i] == BONUS:
            x = reelset[0][i:i+3]
            first_reel_view.append(x)
            break
    reelview =  append_non_win_reel(first_reel_view,reelset)
    x = []
    for j in range(len(reelset[4])):
        if reelset[4][j] == BONUS:
            x = reelset[4][j:j+3]
            break
    reelview.append(x)
    reelview.pop(4)
    # add part for FS
    test_case = get_test_case(reelview,reelset)
    for i in switch_witches:
        test_case.append(i)
    test_case.append(getFSamountWager(FS))

    # add part for MP
    test_case.append(getMultiplierWager(MP))

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
bonus          = raw_input("Do you need bonus test case? Yes/No: ")

if bonus == "Yes" or bonus == "yes" or bonus == "YES":
    FS = input("Enter free spins amount that you what to get(5/7/10/20): ")
    MP = input("Enter size of multiplier that you what to get(2/3/4/5/7/10): ")
    start_time = time.time()
    test_case = get_bonus_test_case(REEL_SET0,FS,MP)
    console_test_case(test_case_name, test_case)

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
