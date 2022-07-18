# all_tables_by_state

| column name    | data type | description                                                     | source     |
|----------------|-----------|-----------------------------------------------------------------|------------|
| year           | string    | program report year                                             | pdf        |
| state          | string    | us state (including DC) with supplemental program               | pdf        |
| liv_arr        | string    | living arrangements defined by state                            | pdf        |
| sub_cat        | string    | sub-category/name of living arrangement                         | pdf        |
| combn_indv     | float     | combined state + federal individual benefits                    | pdf        |
| combn_cpl      | float     | combined state + federal couple benefits                        | pdf        |
| state_indv     | float     | supplemental state individual benefits                          | pdf        |
| state_cpl      | float     | supplemental state couple benefits                              | pdf        |
| fed_indv       | float     | federal individual benefits (combn_indv - state_indv)           | calculated |
| fed_cpl        | float     | federal couple benefits (combn_cpl - state_cpl)                 | calculated |
| state_diff     | float     | supplemental state benefits difference (state_cpl - state_indv) | calculated |
| state_diff_dbl | boolean   | true or false value if state_cpl is double state_indv benefit   | calculated |
