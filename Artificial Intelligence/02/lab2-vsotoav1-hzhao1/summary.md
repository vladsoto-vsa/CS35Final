# Comparing local search methods

You should pick one test case, such as `Lower_48.json`, and do multiple runs for each local search. Be sure to experiment with the default parameter settings to try to get the best results you can.  Then run at least 3 experiments using each search method.


testing using North_America_75.json
TSP "select":"best"

| HC     | Best Cost |
| ------ | --------- |
| run 1  | 355.997   |
| run 2  | 303.814   |
| run 3  | 367.236   |
| Avg    | 342.349   |

HC parameters:
  "runs":2,
  "steps":500,
  "rand_move_prob": 0.25

| SA     | Best Cost |
| ------ | --------- |
| run 1  | 447.934   |
| run 2  | 502.846   |
| run 3  | 467.273   |
| Avg    | 472.684   |

SA parameters:
  "runs":5,
  "steps":2500,
  "init_temp":50,
  "temp_decay":0.99


| BS     | Best Cost |
| ------ | --------- |
| run 1  |  482.115  |
| run 2  |  491.910  |
| run 3  |  535.145  |
| Avg    |  503.056  |

BS parameters:
  "pop_size":50,
  "steps":250,
  "init_temp":200,
  "temp_decay":0.99,
  "max_neighbors":5

-------------------------------------
testing using lower48.json
same parameters

| HC     | Best Cost |
| ------ | --------- |
| run 1  | 764.409   |
| run 2  | 700.779   |
| run 3  | 810.847   |
| Avg    | 758.678   |



| SA     | Best Cost |
| ------ | --------- |
| run 1  | 1617.644  |
| run 2  | 1622.789  |
| run 3  | 1681.231  |
| Avg    | 1640.554  |


| BS     | Best Cost |
| ------ | --------- |
| run 1  |  1970.083 |
| run 2  |  2035.847 |
| run 3  |  1990.716 |
| Avg    |  1998.882 |

-------------------------------
testing using lower48.json
different parameters


| HC     | Best Cost |
| ------ | --------- |
| run 1  | 2851.869  |
| run 2  | 3302.000   |
| run 3  | 3009.520   |
| Avg    | 3054.463   |

HC parameters:
"runs":2,
"steps":150,
"rand_move_prob": 0.75


| SA     | Best Cost |
| ------ | --------- |
| run 1  | 1557.045  |
| run 2  | 1585.269  |
| run 3  | 1624.275  |
| Avg    | 1588.863  |

SA parameters:
"runs":5,
"steps":2500,
"init_temp":10,
"temp_decay":0.99

| BS     | Best Cost |
| ------ | --------- |
| run 1  |  875.729  |
| run 2  |  886.037  |
| run 3  |  987.020  |
| Avg    |  916.262  |

BS parameters:
"pop_size":1000,
"steps":300,
"init_temp":50,
"temp_decay":0.99,
"max_neighbors":10

Which local search algorithm (HC, SA, or BS) most consistently finds the best tours and why do you think it outperforms the others?

It seems BS most consistently finds the best tours. We think it outperforms the others because due to its population size and neighbors size
it's able to cast a wide web across, or several "paths", to find the best costs.
