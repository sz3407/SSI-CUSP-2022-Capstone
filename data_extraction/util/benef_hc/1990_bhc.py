#AZ, 2 insert copies
_copied_benefs = benefs[2][-4:]
_copied_benefs += _copied_benefs
benefs[2] += _copied_benefs

#FL, 8 shuffle
insert = ['N/A', 'N/A', 'N/A']
benefs[8][21:21] = insert
del benefs[8][33:36]

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
benefs[21][12:12] = ['N/A', 'N/A']

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

#OR, 32 insert missing/shuffle
#
#<ABAB> <CDCD> <ABCD> <_BCD> E <FGFGFG_G> (HI) (JK)
#A B C D E F G H I J K
or_insert = ['0']
benefs[32][12:12] = or_insert
benefs[32][26:26] = or_insert
abcd_slice = benefs[32][0:16]
e_slice = benefs[32][16:20]
fg_slice = benefs[32][20:28]
hi_slice = benefs[32][28:36]
jk_slice = benefs[32][36:44]
abcd_idxs = [0, 2, 8, 12, 1, 3, 9, 13, 4, 6, 10, 14, 5, 7, 11, 15]
e_idxs = [1, 0, 3, 2]
abcd_slice = [abcd_slice[idx] for idx in abcd_idxs]
e_slice = [e_slice[idx] for idx in e_idxs]
benefs[32] = abcd_slice + e_slice + fg_slice + hi_slice + jk_slice

#WA, 40 insert missing
#
#<ABABABA_> (CD) E F <GHGHG_GH>
#(AB) (CD) E F (GH)
wa_insert = ['0']
benefs[40][7:7] = wa_insert
benefs[40][29:29] = wa_insert