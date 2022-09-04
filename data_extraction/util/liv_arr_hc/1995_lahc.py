#DC, 7 delete extra table carryover
del liv_arrs[7][7:11]

#FL, 8 remove subcategories, handled in _adjustments
del liv_arrs[8][1]
del liv_arrs[8][2]

#ID, 10 join, delete
liv_arrs[10][3] = liv_arrs[10][3] + liv_arrs[10][4]
del liv_arrs[10][4]

#MN, 20 drop erroneous
liv_arrs[20][2] = liv_arrs[20][2][:-8] #drop ' ll ll 1' (3/ 3/ 3/ 3/)

#OH, 31 delete
del liv_arrs[31][3]

#WI, 42
_front = 'Living in h'
liv_arrs[42][3] = _front + liv_arrs[42][3][1:]
liv_arrs[42][6] = _front + liv_arrs[42][6][1:]
liv_arrs[42][8] = _front + liv_arrs[42][8][1:]