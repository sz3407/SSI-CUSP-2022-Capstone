#several states require `complex` insertion or shuffle to the table data

pattern_footnote_benefs = r"\$[\d]{2}"

#AZ, 2 copy
benefs[2][1:1] = ['570.00']
benefs[2][2:2] = ['70.00']
_copied = benefs[2][4:8]
_copied += _copied
benefs[2][8:8] += _copied

#MD, 17
benefs[17][5:5] = ['-', '-', '-', '-', '-']
benefs[17] += ['-', '-', '-', '-', '-']

#MA, 18
#
benefs[18][3:3] = ['201.72']

#MI, 19 insert missing G G _ _ H H _ _
benefs[19][26:26] = ['9.33', '14.00']
benefs[19] += ['7.00', '14.00']

#MN, 20 insert missing
benefs[20][17:17] = ['N/A']
benefs[20][19:19] = ['N/A']

#MO, 21 insert missing
#
#A B C _ _ DD
#A B C D
benefs[21][12:12] = ['N/A', 'N/A']

#NH, 25 insert missing
#
#A B <CDEFG _ _ _ _ _ CDEFG _ _ _ _ _>
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

#ND, 30
benefs[30][1:1] = ['0']
benefs[30] += ['0']

#RI, 35
benefs[35][9:9] = ['0']
benefs[35][11:11] = ['0']

#UT, 38 insert missing
#
#(AB)
benefs[38][2:2] = ['0']

#VT, 39
benefs[39][29:29] = ['0']
benefs[39] += ['0']

#WA, 41
del benefs[41][15]
benefs[41][11:11] = ['N/A']