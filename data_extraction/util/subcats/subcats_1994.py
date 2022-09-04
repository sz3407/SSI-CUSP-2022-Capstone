# ====================== 1994 ====================== #
_1994_liv_arr_adjs_deltas = [[8, [0, ['Adult foster care', 'Adult congregate living facilities']]], #FL
                             [25, [4, ['Nonsubsidized', 'Subsidized']]]] #NH

for adj in _1994_liv_arr_adjs_deltas:
    liv_arr_adjs[adj[0]] = [adj[1]]

liv_arr_adjs[20] = [[0, ['Entitlement prior to 1994', 'Entitlement 1994 or later']], [1, ['Entitlement prior to 1994', 'Entitlement 1994 or later']]] #MN