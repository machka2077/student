def opredst(array, k):
    if array.count(5)==k:
        s='Повышенная стипендия'
    if (array.count(3)==0) and (array.count(5)!=k):
        s='Обычная стипендия'
    if array.count(3)!=0:
        s='Стипендии нет'
    return s

n=int(input('Введите количество студентов: '))
name=[]
for i in range(n):
    name.append(input("Введите ФИО студента: "))

a=[]
b=[]
k=int(input('Введите количество предметов: ')) 
for i in range(len(name)):
    b=[]
    for j in range(k):
        b.append(int(input("Введите оценку: ")))
    a.append(b)

for i in range(len(name)):
    sr=0
    summ=0
    for j in range(len(a[i])):
        summ+=a[i][j]
        sr=summ/k 
    print(name[i], ':', a[i], 'Средняя оценка: ', sr, 'Стипендия: ', opredst(a[i], k))
    print()








