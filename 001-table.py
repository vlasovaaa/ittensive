N = input("Введите число: ") 
N = int(N)
print('-' * (5 + 4 * N)) 
print('|   |', end ='') 
for i in range (1, N + 1):
    if i < 10: 
        print(' %d |' % (i), end ='') 
    else: 
        print('%d |' % (i), end ='') 
print('') 
print('-' * (5 + 4 * N)) 
for j in range (1, N + 1): 
    if j < 10: 
        print('| %d |'% (j), end ='') 
    else: 
        print('%d |' % (j), end ='') 
    
    for i in range (1, N + 1): 
        if (i * j) < 10: 
            print(' %d |' % (i * j) , end ='') 
        else: 
            print('%d |' % (i * j) , end ='') 

    print('') 
print('-' * (5 + 4 * N))
