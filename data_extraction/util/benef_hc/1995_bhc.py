#several states require `complex` insertion or shuffle to the table data

pattern_footnote_benefs = r"\$[\d]{2}"

#CO, 4 insert missing
benefs[4][5:5] = ['0']

#DC, 7 drop extra table benefs
benefs[7] = benefs[7][:28]

#MI, 19 reorder (GH)
_gh_slice = benefs[19][24:32]
del benefs[19][24:]
_gh_idxs = [0, 1, 2, 4, 6, 7, 3, 5]
_gh_slice = [_gh_slice[idx] for idx in _gh_idxs]
benefs[19] += _gh_slice

#MN, 20 insert missing
#
#A B C D _ _ _ _ F
#A B C D E F
_footnote_benef = re.search(pattern_footnote_benefs, footnotes[20][0]).group()[1:]+'.00'
mn_insert = [_footnote_benef] * 4
benefs[20][16:16] = mn_insert

#MO, 21 insert missing
#
#A B C _ _ DD
#A B C D
mo_insert = ['N/A', 'N/A']
benefs[21][12:12] = mo_insert

#NE, 23 reorder (GHI)
_ghi_slice = benefs[23][24:]
del benefs[23][24:]
_ghi_idxs = [0, 1, 2, 3, 6, 7, 9, 10, 4, 5, 8, 11]
_ghi_slice = [_ghi_slice[idx] for idx in _ghi_idxs]
benefs[23] += _ghi_slice

#NH, 25 insert missing
#
#A B <CDE _ _ _ _ _ CDE _ _ _ _ _>
#A B (CDEFG)
benefs[25][7] = '13.00'
_cdefg1 = benefs[25][8:13]
_cdefg3 = benefs[25][13:18]
_cde2 = [str((float(benef) * 2)) for benef in _cdefg1]
_cde4 = [str((float(benef) * 2)) for benef in _cdefg3]
benefs[25][13:13] = _cde2
benefs[25] += _cde4

#OR, 33 insert missing/shuffle
#
#<ABAB> <CDCD> <ABCD> <_BCD> E (FG) (HI) (JK)
#(ABCD) E (FG) (HI) (JK)
or_insert = ['0']
benefs[33][14:14] = or_insert
benefs[33][26:26] = or_insert
_abcd_slice = benefs[33][:12] + benefs[33][14:16] + benefs[33][17:19]
_e_slice = [benefs[33][idx] for idx in [12, 13, 16, 19]]
_fghijk_slice = benefs[33][20:]
benefs[33] = _abcd_slice + _e_slice + _fghijk_slice

#UT, 38 insert missing
#
#(AB)
benefs[38][2:2] = ['0']

#WA, 41 insert missing
#(AB_) (CD) E F <GHGHG_GH> I J
#(AB) (CD) E F (GH) I J
wa_insert = ['0']
benefs[41][7:7] = wa_insert
benefs[41][28:28] = wa_insert