def opredst(array):
    if array.count(5)==4:
        s = 'Повышенная стипендия'
    if (array.count(3)==0) and (array.count(5)!=4):
        s='Обычная стипендия'
    if (array.count(3)!=0):
        s='Стипендии нет'
    return s

name = ['Ильченко Дарья', 'Крылова Дарья', 'Батыкян Мария']
a = [(5, 5, 5, 5), (4, 4, 4, 5), (4, 3, 5, 5)]
pr = []
pov = []
ob = []
nst = []
k = 0
n = 0
for i in range(len(name)):
    sr = 0
    sum = 0
    for j in range(len(a[i])):
        sum+=a[i][j]
        sr=sum/4
    pr.append(name[i], opredst(a[i]))
    print(name[i], ':', a[i], 'Средняя оценка: ', sr, 'Стипендия: ', opredst(a[i]))

    print()


for i in range(len(pr)):
    if pr[i]=='Повышенная стипендия':
        pov.append(pr[i])
    elif pr(i)=='Обычная стипендия':
        ob.append(pr[i])
    else nst.append(pr[i])
print(pov, )
