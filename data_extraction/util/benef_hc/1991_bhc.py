#several states require `complex` insertion or shuffle to the table data

pattern_footnote_benefs = r"\$[\d]{2}"

#CO, 4 shuffle [C1, D1, E1]
#
#<ABAB> <CDECDE> <ABCDEABCDE> F
#(ABCDE) F
_move = benefs[4][4:7]
benefs[4][2:2] = _move
del benefs[4][7:10]

#IA, 13 fix numerical error
#
# idx[4], 298.34 --> 293.34
# A B (CD) E (FG) H I J
benefs[13][4] = '293.34'

#MA, 18 shuffle [D3, E3, F3] [D4, E4, F4]
#
#(ABC) <DEFDEF> <GHIGHI> <DEF> <GHI> <DEFGHI> (JK) L
#(ABC) (DEF) (GHI) (JK) L
_abc = benefs[18][0:12]
_def12 = benefs[18][12:18]
_def3 = benefs[18][24:27]
_def4 = benefs[18][30:33]
_ghi12 = benefs[18][18:24]
_ghi3 = benefs[18][27:30]
_ghi4 = benefs[18][33:36]
_jk = benefs[18][36:44]
_l = benefs[18][44:48]
benefs[18] = _abc + _def12 + _def3 + _def4 + _ghi12 + _ghi3 + _ghi4 + _jk + _l

#MI, 19 drop second table
#
# A B C D E F G H
benefs[19] = benefs[19][0:int(len(benefs[19]) / 2)]

#MN, 20 insert missing
#
#A B _ _ _ _ D
#A B C D
_footnote_benef = re.search(pattern_footnote_benefs, footnotes[20][0]).group()[1:]+'.00'
mn_insert = [_footnote_benef] * 4
benefs[20][8:8] = mn_insert

#MO, 21 insert missing
#
#A B C _ _ DD
#A B C D
mo_insert = ['N/A', 'N/A']
benefs[21][12:12] = mo_insert

#NH, 25 insert missing
#
#A B <CDE _ _ _ CDE _ _ _>
#A B (CDE)
_cde1 = benefs[25][8:11]
_cde3 = benefs[25][11:14]
_cde2 = [str((float(benef) * 2)) for benef in _cde1]
_cde4 = [str((float(benef) * 2)) for benef in _cde3]
benefs[25][11:11] = _cde2
benefs[25] += _cde4

#NJ, 26 fix many numerical errors
#
_nj_26_fix = ['557.05', '1095.36', '150.05', '485.36', 
              '438.25', '635.36', '31.25', '25.36',
              '635.36', 'N/A', '228.36', 'N/A',
              '635.36', 'N/A', '24.36', 'N/A',
              '315.65', '499.76', '44.31', '93.09',
              '40.00', '80.00', '10.00', '20.00']
benefs[26] = _nj_26_fix

#NY, 28 fix numerical error
#
# idx[34], 28.00 --> 23.00
#A B (CD) (EF) (GH) I J
benefs[28][34] = '23.00'

#OR, 33 insert missing/shuffle
#<ABAB> <CDCD> <ABCD> <_BCD> E <FGFGFG_G> (HI) (JK)
#(ABCD) E (FG) (HI) (JK)
or_insert = ['0']
benefs[33][12:12] = or_insert
benefs[33][26:26] = or_insert
_ab1 = benefs[33][4:6]
_ab2 = benefs[33][6:8]
benefs[33][0:0] = _ab1
benefs[33][4:4] = _ab2
del benefs[33][8:12]

#RI, 35 shuffle CD
#
# A B <CDCDCCDD>
# A B (CD)
benefs[35].insert(13, '10.00')
del benefs[35][15]

#WA, 41 insert missing
#<ABABABA_> (CD) E F <GHGHG_GH>
#(AB) (CD) E F (GH)
wa_insert = ['0']
benefs[41][7:7] = wa_insert
benefs[41][29:29] = wa_insert

#WI, 42 fix numerical error; shuffle [HI]
#
# A B C D E F G (HI)
benefs[42][0] = '509.72'
_copy = benefs[42][29]
benefs[42][33:33] = [_copy]
del benefs[42][29]