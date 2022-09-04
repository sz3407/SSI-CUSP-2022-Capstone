#several states require `complex` insertion or shuffle to the table data

pattern_footnote_benefs = r"\$[\d]{2}"

#ID, 10 reorder A (BCDEF) G
a_slice = benefs[10][0:4]
g_slice = benefs[10][19:23]
del benefs[10][19:23]
_bcdef_slice = benefs[10][4:24]
_bcdef_idxs = [0, 2, 6, 7, 8, 1, 3, 9, 10, 11, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19]
_bcdef_slice = [_bcdef_slice[idx] for idx in _bcdef_idxs]
benefs[10] = a_slice + _bcdef_slice + g_slice

#MN, 20 insert missing
#
#A B _ _ _ _ D
#A B C D
_b1 = benefs[20][2]
del benefs[20][2]
benefs[20][1:1] = [_b1]
_footnote_benef = re.search(pattern_footnote_benefs, footnotes[20][0]).group()[1:]+'.00'
mn_insert = [_footnote_benef] * 4
benefs[20][16:16] = mn_insert

#MO, 21 insert missing
#
#A B C _ _ DD
#A B C D
mo_insert = ['N/A', 'N/A']
benefs[21][12:12] = mo_insert

#NH, 25 insert missing
#
#A B <CDE _ _ _ _ _ CDE _ _ _ _ _>
#A B (CDEFG)
_cdefg1 = benefs[25][8:13]
_cdefg3 = benefs[25][13:18]
_cde2 = [str((float(benef) * 2)) for benef in _cdefg1]
_cde4 = [str((float(benef) * 2)) for benef in _cdefg3]
benefs[25][13:13] = _cde2
benefs[25] += _cde4

#NJ, 26 swap/delete
#
#A B <CDCD> <EEFF> <CDEF> <CDEF>
#A B (CDEF)
_ef1 = [benefs[26][12], benefs[26][14]]
del benefs[26][12]
del benefs[26][13]
benefs[26][10:10] = _ef1

#OR, 33 insert missing/shuffle
#
#<ABAB> <CDCD> <ABCD> <_BCD> E (FG) (HI) (JK)
#(ABCD) E (FG) (HI) (JK)
or_insert = ['0']
benefs[33][12:12] = or_insert
benefs[33][26:26] = or_insert
_cd1 = benefs[33][4:6]
del benefs[33][4:6]
benefs[33][2:2] = _cd1

#RI, 35 shuffle CD
#
# A B <CDCDCCDD>
# A B (CD)
benefs[35].insert(13, '10.00')
del benefs[35][15]

#UT, 38 drop second table
#
#(AB)
benefs[38] = benefs[38][0:8]

#WA, 41 insert missing
#(AB_) (CD) E F <GHGHG_GH> I J
#(AB) (CD) E F (GH) I J
wa_insert = ['0']
benefs[41][7:7] = wa_insert
benefs[41][28:28] = wa_insert
_f4 = benefs[41][31]
del benefs[41][31]
benefs[41][23:23] = [_f4]