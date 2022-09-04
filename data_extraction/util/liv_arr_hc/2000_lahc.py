#AZ, 2
_az0 = liv_arrs[2][0]
_az2 = liv_arrs[2][2]
_split_arrs = [cap_first(drop_or(ele).lstrip()) for ele in liv_arrs[2][1].split(',')]
liv_arrs[2] = [_az0] + _split_arrs + [_az2]

#FL, 8 remove subcategories, handled in _adjustments
del liv_arrs[8][1]

#ID, 10 join, delete
liv_arrs[10][3] = liv_arrs[10][3] + liv_arrs[10][4]
del liv_arrs[10][4]

#MN, 20
liv_arrs[20][2] = drop_comma(liv_arrs[20][2])

#NY, 28 drop erroneous characters
liv_arrs[28][2] = liv_arrs[28][2] + " I"
liv_arrs[28][3] = liv_arrs[28][3] + " II" 
liv_arrs[28][4] = liv_arrs[28][4] + " III"

#NC, 29 join, delete
liv_arrs[29][1] = liv_arrs[29][1] + " SSI"

#ND, 30
liv_arrs[30][0] += " Basic Care Facility"

#VT, 39
liv_arrs[39][4] = drop_comma(liv_arrs[39][4])

#WI, 42
_front = 'Living in h'
liv_arrs[42][3] = _front + liv_arrs[42][3][1:]
liv_arrs[42][6] = _front + liv_arrs[42][6][1:]
liv_arrs[42][8] = _front + liv_arrs[42][8][1:]