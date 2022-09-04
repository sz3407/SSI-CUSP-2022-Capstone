#several states require `complex` insertion or shuffle to the table data

pattern_footnote_benefs = r"\$[\d]{2}"

#AK
benefs[1] += ['45.00', '90.00']

#AZ
benefs[2][1:1] = ['N/A']
benefs[2][3:3] = ['N/A']
_copied = benefs[2][4:8]
benefs[2][8:8] += _copied

#CO, 4 insert missing
benefs[4][5:5] = ['0']

#ID, 10 shuffle (BCDEF) G
_a_slice = benefs[10][0:4]
_g_slice = benefs[10][19:23]
del benefs[10][19:23]
_bcdef_slice = benefs[10][4:]
_bcdef_idxs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 11, 13, 17, 18, 19]
_bcdef_slice = [_bcdef_slice[idx] for idx in _bcdef_idxs]
benefs[10] = _a_slice + _bcdef_slice + _g_slice

#KY
benefs[14][5:5] = ['139.00']
del benefs[14][7]

#MI, 19 insert missing G G _ _ H H _ _
benefs[19][26:26] = ['9.33', '14.00']
benefs[19] += ['7.00', '14.00']

#MO, 21 insert missing
#
#A B C _ _ DD
#A B C D
benefs[21][12:12] = ['N/A', 'N/A']

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
_e1 = benefs[26][12]
_e2 = benefs[26][13]
del benefs[26][12]
del benefs[26][13]
benefs[26][10:10] = _e1
benefs[26][13:13] = _e2

#NC
_de3 = benefs[29][16:18]
del benefs[29][16:18]
benefs[29][13:13] += _de3

#OR, 33 insert missing, isolate E, shuffle C1D1
#
#<ABAB> <CDCD> <ABCD> <EE_BEECD> (FG_) (HI) (JK)
#(ABCD) E (FG) (HI) (JK)
benefs[33][12:12] = ['0']
benefs[33][26:26] = ['0']
_abcd_slice = benefs[33][:16]
_abcd_idxs = [4, 5, 0, 1, 6, 7, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]
_abcd_slice = [_abcd_slice[idx] for idx in _abcd_idxs]
_efghijk_slice = benefs[33][16:]
benefs[33] = _abcd_slice + _efghijk_slice

#PA
_b34 = benefs[34][8:10]
del benefs[34][8:10]
benefs[34][6:6] += _b34

#UT, 38 insert missing
#
#(AB)
benefs[38][4:4] = ['0']

#VA, 40 drop second table
del benefs[40][16:]

#WA, 41 insert missing
#(AB_) (CD) E F <GHGHG_GH> I J
#(AB) (CD) E F (GH) I J
benefs[41][7:7] = ['0']
benefs[41][28:28] = ['0']
_e123 = benefs[41][8:11]
benefs[41][19:19] += _e123
del benefs[41][8:11]