import unittest
import Methods_All as source


class TestGetSymbolIndecies(unittest.TestCase):

    def test_border(self):
        test_reel = [1,0,1]
        test_symbol = 1
        test_res = source.get_symbol_indecies(test_reel,test_symbol)
        expected_result = [0,2]
        self.assertEqual(expected_result,test_res)

    def test_random(self):
        test_reel = [1, 0, 0, 1, 10, 1, 5, 1, 0]
        test_symbol = 1
        test_res = source.get_symbol_indecies(test_reel, test_symbol)
        expected_result = [0,3,5,7]
        self.assertEqual(expected_result,test_res)

    def test_ifnoSymbol(self):
        test_reel = [1, 0, 0, 1, 10, 1, 5, 1, 0]
        test_symbol = 9
        test_res = source.get_symbol_indecies(test_reel, test_symbol)
        expected_result = []
        self.assertEqual(expected_result,test_res)


class TestGetLineCombination(unittest.TestCase):

    def test_line3(self):
        combination = [0,0,0,0,0]
        line = source.LINE3
        expected_result = [0,0,0,0,0]
        actual_result = source.get_line_combination(combination, line)
        self.assertEqual(actual_result,expected_result)

    def test_line1(self):
        combination = [2,2,2,2,2]
        line = source.LINE1
        expected_result =[1,1,1,1,1]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line2(self):
        combination = [2,2,2,2,2]
        line = source.LINE2
        expected_result = [0,0,0,0,0]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line4(self):
        combination = [2,2,2,2,2]
        line = source.LINE4
        expected_result = [2,1,0,1,2]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line5(self):
        combination = [2,2,2,2,2]
        line = source.LINE5
        expected_result = [0,1,2,1,0]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line6(self):
        combination = [2,2,2,2,2]
        line = source.LINE6
        expected_result = [1,2,2,2,1]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line7(self):
        combination = [2,2,2,2,2]
        line = source.LINE7
        expected_result = [1,0,0,0,1]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line8(self):
        combination = [2,2,2,2,2]
        line = source.LINE8
        expected_result = [2,2,1,0,0]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line9(self):
        combination = [2,2,2,2,2]
        line = source.LINE9
        expected_result = [0,0,1,2,2]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line10(self):
        combination = [2,2,2,2,2]
        line = source.LINE10
        expected_result = [1,2,1,0,1]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line11(self):
        combination = [2,2,2,2,2]
        line = source.LINE11
        expected_result = [1,0,1,2,1]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line12(self):
        combination = [0,0,0,0,0]
        line = source.LINE12
        expected_result = [0,-1,-1,-1,0]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line13(self):
        combination = [2,2,2,2,2]
        line = source.LINE13
        expected_result = [0,1,1,1,0]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line14(self):
        combination = [2,2,2,2,2]
        line = source.LINE14
        expected_result = [2,1,2,1,2]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line15(self):
        combination = [2,2,2,2,2]
        line = source.LINE15
        expected_result = [0,1,0,1,0]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line16(self):
        combination = [2,2,2,2,2]
        line = source.LINE16
        expected_result = [1,1,2,1,1]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line17(self):
        combination = [2,2,2,2,2]
        line = source.LINE17
        expected_result = [1,1,0,1,1]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line18(self):
        combination = [2,2,2,2,2]
        line = source.LINE18
        expected_result = [2,2,0,2,2]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line19(self):
        combination = [2,2,2,2,2]
        line = source.LINE19
        expected_result = [0,0,2,0,0]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)

    def test_line20(self):
        combination = [2,2,2,2,2]
        line = source.LINE20
        expected_result = [2,0,0,0,2]
        actual_result = source.get_line_combination(combination,line)
        self.assertEqual(actual_result,expected_result)


class TestGetReelCaseFromCombination(unittest.TestCase):

    def test_first_elements_of_reels(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        combination = [0,0,0,0,0]
        expected_result = [[1,2,3],
                           [1,2,3],
                           [1,2,3],
                           [1,2,3],
                           [1,2,3]]
        actual_result = source.getReelCaseFromComb(reelset,combination)
        self.assertEqual(actual_result,expected_result)

    def test_last_elements_of_reels(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        combination = [-1,-1,-1,-1,-1]
        expected_result = [[10,1,2],
                           [10,1,2],
                           [10,1,2],
                           [10,1,2],
                           [10,1,2]]
        actual_result = source.getReelCaseFromComb(reelset,combination)
        self.assertEqual(actual_result,expected_result)

    def test_last_elements_of_reels2(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        combination = [-2,-2,-2,-2,-2]
        expected_result = [[9,10,1],
                           [9,10,1],
                           [9,10,1],
                           [9,10,1],
                           [9,10,1]]
        actual_result = source.getReelCaseFromComb(reelset,combination)
        self.assertEqual(actual_result,expected_result)

    def test_last_elements_of_reels3(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        combination = [9,9,9,9,9]
        expected_result = [[10,1,2],
                           [10,1,2],
                           [10,1,2],
                           [10,1,2],
                           [10,1,2]]
        actual_result = source.getReelCaseFromComb(reelset,combination)
        self.assertEqual(actual_result,expected_result)

    def test_last_elements_of_reels4(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        combination = [8,8,8,8,8]
        expected_result = [[9,10,1],
                           [9,10,1],
                           [9,10,1],
                           [9,10,1],
                           [9,10,1]]
        actual_result = source.getReelCaseFromComb(reelset,combination)
        self.assertEqual(actual_result,expected_result)

    def test_combined_elements_of_6reels(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        combination = [-1,-2,0,8,9,5]
        expected_result = [[10,1,2],
                           [9,10,1],
                           [1,2,3],
                           [9,10,1],
                           [10,1,2],
                           [6,7,8]]
        actual_result = source.getReelCaseFromComb(reelset,combination)
        self.assertEqual(actual_result,expected_result)


class TestGetCombIndex(unittest.TestCase):


    def test1(self):
        reel = [1,2,3,4,5,6,7,8,9,10]
        comb = [1,2,3]
        expected_result = 0
        actual_result = source.get_comb_index(comb,reel)
        self.assertEqual(actual_result,expected_result)

    def test2(self):
        reel = [1,2,3,4,5,6,7,8,9,10]
        comb = [10,1,2]
        expected_result = 9
        actual_result = source.get_comb_index(comb,reel)
        self.assertEqual(actual_result,expected_result)

    def test3(self):
        reel = [1,2,3,4,5,6,7,8,9,10]
        comb = [9,10,1]
        expected_result = 8
        actual_result = source.get_comb_index(comb,reel)
        self.assertEqual(actual_result,expected_result)

    def test4(self):
        reel = [1,2,3,4,5,6,7,8,9,10]
        comb = [9,10,8]
        expected_result = 8
        actual_result = source.get_comb_index(comb,reel)
        self.assertIsNot(actual_result,expected_result)


class TestGetTestCase(unittest.TestCase):

    def test5reels_difrntPos(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        reelcase = [[1,2,3],
                    [10,1,2],
                    [9,10,1],
                    [2,3,4],
                    [8,9,10]]
        expected_result = [None, 0,9,8,1,7]
        actual_result = source.get_test_case(reelcase,reelset)
        self.assertEqual(actual_result,expected_result)

    def test2reels_difPos(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        reelcase = [[1,2,3],
                    [10,1,2]]
        expected_result = [None, 0,9]
        actual_result = source.get_test_case(reelcase,reelset)
        self.assertEqual(actual_result,expected_result)

    def test6reels_difrntPos(self):
        reelset = [[1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        reelcase = [[1,2,3],
                    [10,1,2],
                    [9,10,1],
                    [2,3,4],
                    [8,9,10],
                    [8,9,10]]
        expected_result = [None, 0,9,8,1,7,7]
        actual_result = source.get_test_case(reelcase,reelset)
        self.assertEqual(actual_result,expected_result)

    def test5reels_2simReelcombs(self):
        reelset = [[1,2,3,1,2,3,7,8,9,10],
                   [1,2,10,1,2,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        reelcase = [[1,2,3],
                    [10,1,2],
                    [9,10,1],
                    [2,3,4],
                    [8,9,10]]
        expected_result = [None, 0,2,8,1,7]
        actual_result = source.get_test_case(reelcase,reelset)
        self.assertEqual(actual_result,expected_result)

    def test5reels_noSymbols(self):
        reelset = [[1,2,3,1,2,3,7,8,9,10],
                   [1,2,10,1,2,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10],
                   [1,2,3,4,5,6,7,8,9,10]]
        reelcase = [[11,12,13],
                    [11,11,12],
                    [19,11,11],
                    [12,13,14],
                    [18,19,11]]
        expected_result = [None, None,None,None,None,None]
        actual_result = source.get_test_case(reelcase,reelset)
        self.assertEqual(actual_result,expected_result)


class Testlineview(unittest.TestCase):

    def testLine1(self):
        line = source.LINE1
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [2,5,8,11,14]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine2(self):
        line = source.LINE2
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [3,6,9,12,15]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine3(self):
        line = source.LINE3
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [1,4,7,10,13]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine4(self):
        line = source.LINE4
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [1,5,9,11,13]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine5(self):
        line = source.LINE5
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [3,5,7,11,15]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine6(self):
        line = source.LINE6
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [2,4,7,10,14]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine7(self):
        line = source.LINE7
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [2,6,9,12,14]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine8(self):
        line = source.LINE8
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [1,4,8,12,15]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine9(self):
        line = source.LINE9
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [3,6,8,10,13]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine10(self):
        line = source.LINE10
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [2,4,8,12,14]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine11(self):
        line = source.LINE11
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [2,6,8,10,14]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine12(self):
        line = source.LINE12
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [1,5,8,11,13]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine13(self):
        line = source.LINE13
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [3,5,8,11,15]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine14(self):
        line = source.LINE14
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [1,5,7,11,13]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine15(self):
        line = source.LINE15
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [3,5,9,11,15]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine16(self):
        line = source.LINE16
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [2,5,7,11,14]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine17(self):
        line = source.LINE17
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [2,5,9,11,14]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine18(self):
        line = source.LINE18
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [1,4,9,10,13]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine19(self):
        line = source.LINE19
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [3,6,7,12,15]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)

    def testLine20(self):
        line = source.LINE20
        reelcase = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15]]
        expected_result = [1,6,9,12,13]
        actual_result = source.lineview(line, reelcase)
        self.assertEqual(actual_result,expected_result)


if __name__ == '__main__':
    unittest.main()