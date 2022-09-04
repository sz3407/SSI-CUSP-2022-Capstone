#AZ, 2
_split_arrs = [cap_first(drop_or(ele).lstrip()) for ele in liv_arrs[2][3].split(',')]
liv_arrs[2] = liv_arrs[2][:3] + _split_arrs

#CA, 3
liv_arrs[3][4] = insert_slash(drop_or(liv_arrs[3][4]))
liv_arrs[3][5] = drop_comma(liv_arrs[3][5])

#FL, 8
liv_arrs[8][0] = liv_arrs[8][0] + ' (' + liv_arrs[8][1] + ')'
liv_arrs[8][4] = liv_arrs[8][4] + ' (' + liv_arrs[8][5] + ')'
del liv_arrs[8][1]
del liv_arrs[8][4]

#HI, 9 
liv_arrs[9][3] = liv_arrs[9][3][:-2]

#IA, 13
liv_arrs[13][5] = liv_arrs[13][3]

#MI, 19 drop second table
liv_arrs[19] = liv_arrs[19][:8]

#MN, 20
liv_arrs[20][2] = drop_comma(liv_arrs[20][2])

#NJ, 26
liv_arrs[26][0] = liv_arrs[26][0][:-1]

#NY, 28
liv_arrs[28][2] = liv_arrs[28][2] + " I"
liv_arrs[28][3] = liv_arrs[28][3] + " II"
liv_arrs[28][4] = liv_arrs[28][4][:-4] + " III"

#NC, 29
liv_arrs[29][2] = liv_arrs[29][2] + " SSI"

#WI, 42
_front = 'Living in h'
liv_arrs[42][3] = _front + liv_arrs[42][3][1:]
liv_arrs[42][6] = _front + liv_arrs[42][6][1:]
liv_arrs[42][8] = _front + liv_arrs[42][8][1:]