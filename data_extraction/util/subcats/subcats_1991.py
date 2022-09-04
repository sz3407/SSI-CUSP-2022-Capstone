# ====================== 1991 ====================== #
_1991_liv_arr_adjs_deltas = [[17, [0, ['Minimal supervision', 'Moderate supervision', 'Extensive supervision', 'Specialized and intensive services']]]] #MD

for adj in _1991_liv_arr_adjs_deltas:
    liv_arr_adjs[adj[0]] = [adj[1]]
    
#insert empty [] for ND
liv_arr_adjs.insert(30, [])