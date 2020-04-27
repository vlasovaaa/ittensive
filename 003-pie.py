import pandas as pd 
students = pd.read_csv('http://xn----8sblcdzzacvuc0jbg.xn--80abucjiibhv9a.xn--p1ai/opendata/7710539135-VPO/data-20141202-structure-20141202.csv', sep=';') 
all = (students['countstudentgos'].sum() + students['countstudentnegos'].sum()) 
import matplotlib.pyplot as plt 
pieses = [students['countstudentnegos'].sum(), students['countstudentgos'].sum()] 
owners = ['Студенты негосуд.вузов', 'Остальные'] 
cols = ['b','r'] 
plt.pie(pieses, labels = owners, colors = cols, shadow = 1, explode = (0.1, 0), autopct='%.1f') 
plt.title('Процент студентов, обучающих в негосударственных ВУЗах относительно общего числа студентов') 
plt.show()
