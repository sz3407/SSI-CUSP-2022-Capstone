#several states require `complex` insertion or shuffle to the table data

pattern_footnote_benefs = r"\$[\d]{2}"

#CO, 4 reorder (ABCDE)
#
#<ABAB> <CCABC> <DEDEDE> <ABCDE> F
#(ABCDE) F
abcde_slice = benefs[4][0:20]
f_slice = benefs[4][20:24]
abcde_idxs = [0, 1, 4, 9, 10, 2, 3, 5, 11, 12, 6, 7, 8, 13, 14, 15, 16, 17, 18, 19]
abcde_slice = [abcde_slice[idx] for idx in abcde_idxs]
benefs[4] = abcde_slice + f_slice

#MA, 18 shuffle [G1, H1, I1]
#
#(ABC) <DEFDEF> <GHIGHI> <DEFGHI> <DEFGHI> (JK) L
#(ABC) (DEFGHI) (JK) L
_ghi1 = benefs[18][18:21]
benefs[18][15:15] =  _ghi1
del benefs[18][21:24]

#MI, 19 insert missing
#
# A B C D E F G H
_g34 = ['9.33', '14.00']
_h34 = ['7.00', '14.00']
benefs[19][26:26] = _g34
benefs[19][len(benefs[19]):len(benefs[19])] = _h34

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
#A B <CDCD> <EEFF> <CDEF> <CDEF>
#A B (CDEF)
_ef1 = [benefs[26][12], benefs[26][14]]
del benefs[26][12]
del benefs[26][13]
benefs[26][10:10] = _ef1

#OR, 33 insert missing/shuffle
#
#<ABCD>3 <ABCD>4 <DABABCDC> %E% <FGFGFG_G> (HI) (JK)
#A B C D E F G H I J K
or_insert = ['0']
benefs[33][4:4] = or_insert
benefs[33][26:26] = or_insert
abcd_slice = benefs[33][0:16]
e_slice = benefs[33][16:20]
fghijk_slice = benefs[33][20:44]
abcd_idxs = [9, 10, 13, 14, 11, 12, 15, 7, 0, 1, 2, 3, 4, 5, 6, 8]
e_idxs = [1, 2, 3, 0]
abcd_slice = [abcd_slice[idx] for idx in abcd_idxs]
e_slice = [e_slice[idx] for idx in e_idxs]
benefs[33] = abcd_slice + e_slice + fghijk_slice

#WA, 41 insert missing
#<ABABABA_> (CD) E F <GHGHG_GH>
#(AB) (CD) E F (GH)
wa_insert = ['0']
benefs[41][7:7] = wa_insert
benefs[41][29:29] = wa_insert