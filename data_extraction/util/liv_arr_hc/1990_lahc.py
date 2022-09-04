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
liv_arrs[9][2] = liv_arrs[9][2][:-2] #drop ' n' (II)
liv_arrs[9][3] = liv_arrs[9][3][:-2] #drop ' m' (III)

#MN, 20
liv_arrs[20][2] = drop_comma(liv_arrs[20][2])

#MO, 21
liv_arrs[21][1] = liv_arrs[21][1][:-3] #drop ' ll' (II)

#NY, 28
liv_arrs[28][2] = liv_arrs[28][2] + " I"
liv_arrs[28][3] = liv_arrs[28][3] + " II"
liv_arrs[28][4] = liv_arrs[28][4][:-2] + " III"

#NC, 29
liv_arrs[29][2] = liv_arrs[29][2] + " SSI"

#OR, 32
liv_arrs[32][4] = insert_slash(liv_arrs[32][4])

#VT, 38
liv_arrs[38][2:5] = ['Custodial-care', 'Custodial-care', 'Custodial-care']

#WI, 41
_front = 'Living in h'
liv_arrs[41][3] = _front + liv_arrs[41][3][1:] #adjust leading phrase
liv_arrs[41][6] = _front + liv_arrs[41][6][1:]
liv_arrs[41][8] = _front + liv_arrs[41][8][1:]