with open ('students.tsv', 'r') as students: 
data = [] #будет список всех оценок 
b = 0 #количество студентов выше среднего 
no_line = 0 #количество строк=количество студентов 
for line in students: 
    no_line += 1 
    items = line.split() 
    i = 1 
    summa = 0 
    while i < len(items): 
        summa += int(items[i]) 
	data.append(int(items[i])) 
	i += 1 
	average = summa / (i - 1) 
    if average > 4.5: 
	b += 1 
	print('Преуспевающие студенты: ' + str(items[0])) 
    elif average < 2.5: 
	print('Студенты к отчислению: ' + str(items[0]))  
    elif average > sum(data)/len(data): 
        b += 1 
five = data.count(5) 
four = data.count(4) 
three = data.count(3) 
two = data.count(2) 
quality = (five + four) / len(data) 
learn = ( five + four * 0.64 + three * 0.36 + two * 0.16 ) / len(data) 
proz = (b / no_line) * 100 #рассчитываем процент студентов выше среднего 
print('Качество обучения: ' + str(quality)) 
print('Обученность: ' + str(learn)) 
print('Студенты с баллом выше среднего: ' + str(proz) + '%')
print('Средний балл по всем студентам: ' + str(sum(data)/len(data))
result = open('result.txt', 'w') 
result.write(str(proz))
