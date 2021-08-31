# Try on a randomy generated much larger dataset
import numpy as np
import scipy as sp
import pandas as pd
import random
import time


### # cell 1
np_persons = 100_000
nb_days = 1_095
data = pd.DataFrame()
columns = []
for i in range(np_persons):
    one_person_nb_days_stay = sp.random.binomial(1095, 0.01)
    days = np.zeros(1095)
    days[np.random.choice(range(len(days)), one_person_nb_days_stay, replace=False)] = 1
    columns.append(pd.Series(days, name=f"P{i}"))
     
data= pd.DataFrame({x.name: x  for x in columns})



### cell 2
nb_hotels = 60
hotel_ids = np.array(range(1, nb_hotels+1))
x = np.random.pareto(2, nb_hotels)
list_of_rows = []

for row in range(data.shape[0]):
    sum_in_hotels = sum(data.iloc[row, : ])

    x = np.random.pareto(2, nb_hotels)

    occupancy = np.random.multinomial(sum_in_hotels, x/sum(x))
    status = np.zeros(np_persons)
    repeats = np.repeat(hotel_ids, occupancy)
    positions = np.where(data.iloc[row, :] != 0)[0]
    status[positions] = repeats

    list_of_rows.append(status)
    
    if row % 200 == 0:
        print(row)
        
final_data = pd.DataFrame(list_of_rows)

final_data.columns = data.columns
