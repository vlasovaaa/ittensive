with open('temp_data.csv', 'r') as data:
    j = 0 
    for line in data: 
        j += 1 
        items = line.strip('').split(";") 
        i = 0 
        sum = [] 
    while i < len(items): 
        sum.append(items[i]) 
        i += 1
import numpy as np
sum = np.array(sum).astype(np.float) 
mean = np.mean(sum) 
delta = np.std(sum, ddof=1) 
print(str(j) + ' января ' + (str(mean.round(2)) + ' +/- ' + str(delta.round(2))))


