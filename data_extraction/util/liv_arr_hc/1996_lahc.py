#remove ID page 2 - autofixes indexes for below
del liv_arrs[11]

#FL, 8 remove subcategories, handled in _adjustments
del liv_arrs[8][1]
del liv_arrs[8][2]

#ID, 10 join, delete
liv_arrs[10][3] = liv_arrs[10][3] + liv_arrs[10][4]
del liv_arrs[10][4]

#IN, 12 drop erroneous
liv_arrs[12] = liv_arrs[12][:1]

#NY, 28 drop erroneous characters
liv_arrs[28][3] = liv_arrs[28][3][:-3] #drop " 11" (II)
liv_arrs[28][4] = liv_arrs[28][4][:-4] #drop " ill" (III)

#NC, 29 join, delete
liv_arrs[29][0] = liv_arrs[29][0] + " " + liv_arrs[29][1]
del liv_arrs[29][1]

#VA, 40 drop "second table"
liv_arrs[40] = liv_arrs[40][0:2]

#WI, 42
_front = 'Living in h'
liv_arrs[42][3] = _front + liv_arrs[42][3][1:]
liv_arrs[42][6] = _front + liv_arrs[42][6][1:]
liv_arrs[42][8] = _front + liv_arrs[42][8][1:]