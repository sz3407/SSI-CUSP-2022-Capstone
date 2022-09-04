#several states require `complex` insertion or shuffle to the table data

#drop ID second table
del benefs[11]

pattern_footnote_benefs = r"\$[\d]{2}"

#CO, 4 insert missing
benefs[4][5:5] = ['0']

#DC, 7 insert missing, shuffle (EFG)
benefs[7][22:22] = ['0']
_efg_slice = benefs[7][16:]
del benefs[7][16:]
_efg_idxs = [0, 2, 4, 1, 3, 5, 6, 7, 8, 9, 10, 11]
_efg_slice = [_efg_slice[idx] for idx in _efg_idxs]
benefs[7] += _efg_slice

#ID, 10 shuffle (BCDEF) G
_a_slice = benefs[10][0:4]
_g_slice = benefs[10][19:23]
del benefs[10][19:23]
_bcdef_slice = benefs[10][4:]
_bcdef_idxs = [0, 2, 6, 7, 8, 1, 3, 9, 10, 11, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19]
_bcdef_slice = [_bcdef_slice[idx] for idx in _bcdef_idxs]
benefs[10] = _a_slice + _bcdef_slice + _g_slice

#MA, 18 shuffle middle
_abc_slice = benefs[18][0:12]
_defghi_slice = benefs[18][12:36]
_jkl_slice = benefs[18][36:]
_defghi_idxs = [0, 1, 2, 6, 7, 8, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
_defghi_slice = [_defghi_slice[idx] for idx in _defghi_idxs]
benefs[18] = _abc_slice + _defghi_slice + _jkl_slice

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
_ef1 = [benefs[26][12], benefs[26][14]]
del benefs[26][12]
del benefs[26][13]
benefs[26][10:10] = _ef1

#OR, 33 insert missing, isolate E, shuffle C1D1
#
#<ABAB> <CDCD> <ABCD> <EE_BEECD> (FG_) (HI) (JK)
#(ABCD) E (FG) (HI) (JK)
benefs[33][14:14] = ['0']
benefs[33][26:26] = ['0']
_abcd_slice = benefs[33][:12] + benefs[33][14:16] + benefs[33][18:20]
_cd1 = benefs[33][4:6]
del _abcd_slice[4:6]
_abcd_slice[2:2] = _cd1
_e_slice = benefs[33][12:14] + benefs[33][16:18]
_fghijk_slice = benefs[33][20:]
benefs[33] = _abcd_slice + _e_slice + _fghijk_slice

#UT, 38 insert missing
#
#(AB)
benefs[38][4:4] = ['0']
_b2 = benefs[38][2]
del benefs[38][2]
benefs[38][1:1] = _b2

#VA, 40 drop second table
del benefs[40][16:]

#WA, 41 insert missing
#(AB_) (CD) E F <GHGHG_GH> I J
#(AB) (CD) E F (GH) I J
benefs[41][7:7] = ['0']
benefs[41][28:28] = ['0']
benefs[41][23:23] = ['N/A']