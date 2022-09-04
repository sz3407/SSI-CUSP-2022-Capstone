#several states require `complex` insertion or shuffle to the table data

pattern_footnote_benefs = r"\$[\d]{2}"

#AZ, 2 copy
_copied = benefs[2][4:8]
_copied += _copied
benefs[2][8:8] += _copied

#CO, 4 insert missing
benefs[4][5:5] = ['0']

#CT, 5
benefs[5] += ['0', '0']

#MA, 18
#
# (ABC) (DEF) (GHI) (JK) L
_abc = benefs[18][:12]
_def12 = benefs[18][12:18]
_ghi12 = benefs[18][18:24]
_def34 = benefs[18][24:30]
_ghi34 = benefs[18][30:36]
_jkl = benefs[18][36:]
benefs[18] = _abc + _def12 + _def34 + _ghi12 + _ghi34 + _jkl

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
#A B <CDCD> <EE> <CDE> <CDE> F
#A B (CDE) F
_e1 = benefs[26][12]
del benefs[26][12]
benefs[26][10:10] = [_e1]

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
benefs[38][2:2] = ['0']

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