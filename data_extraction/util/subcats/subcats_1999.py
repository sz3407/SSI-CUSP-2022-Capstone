# ====================== 1999 ====================== #
_1999_liv_arr_adjs_deltas = [[8, [0, ['Adult family care homes']]]] #FL

for adj in _1999_liv_arr_adjs_deltas:
    liv_arr_adjs[adj[0]] = [adj[1]]
    
liv_arr_adjs[9] = [[1, ['(1 to 5 residents)']], [2, ['(6 or more residents)']]] #HI
liv_arr_adjs[29] = [[0, ['Basic', 'Disenfranchised-ambulatory', 'Disenfranchised-semi-ambulatory']], [1, ['Not paying shelter/utilities', 'Paying shelter/utilities']]] #NC