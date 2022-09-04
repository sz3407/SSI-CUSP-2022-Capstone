#FL, 8
liv_arrs[8][0] = liv_arrs[8][0] + ', ' + liv_arrs[8][1]
liv_arrs[8][4] = liv_arrs[8][4] + ', ' + liv_arrs[8][5]

del liv_arrs[8][1]
del liv_arrs[8][4]

#ID, 10
liv_arrs[10][3] = liv_arrs[10][3] + liv_arrs[10][4]
del liv_arrs[10][4]

#NY, 28 erroneous
liv_arrs[28][4] = liv_arrs[28][4][:-4] #drop ' ill' (III)

#WI, 42
_front = 'Living in h'
liv_arrs[42][3] = _front + liv_arrs[42][3][1:]
liv_arrs[42][6] = _front + liv_arrs[42][6][1:]
liv_arrs[42][8] = _front + liv_arrs[42][8][1:]