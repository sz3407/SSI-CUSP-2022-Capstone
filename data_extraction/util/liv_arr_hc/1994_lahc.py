#FL, 8
del liv_arrs[8][1]
del liv_arrs[8][2]

#HI, 9
liv_arrs[9][3] = liv_arrs[9][3][:-2] #drop ' m' (III) 

#ID, 10
liv_arrs[10][3] = liv_arrs[10][3] + liv_arrs[10][4]
del liv_arrs[10][4]

#IN, 12
del liv_arrs[12][1:]

#NY, 28 erroneous
liv_arrs[28][4] = liv_arrs[28][4][:-4] #drop ' ill' (III)

#UT, 38
liv_arrs[38] = liv_arrs[38][:2]

#WI, 42
_front = 'Living in h'
liv_arrs[42][3] = _front + liv_arrs[42][3][1:]
liv_arrs[42][6] = _front + liv_arrs[42][6][1:]
liv_arrs[42][8] = _front + liv_arrs[42][8][1:]