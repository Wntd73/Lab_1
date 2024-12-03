
from random import randint
K = int(input('Введите число K: '))
N = int(input('Введите целое число N от 3 до 100: '))
while True:
    if N<100 and N>2: break
    else: N=int(input('Введите целое число N от 3 до 100: '))
A,F = [], []
for i in range(N): #создание пустых матриц
    A.append([0]*N)
    F.append([0]*N)
print('Как Вы хотите заполнить матрицу?\n1 - из файла 2 - случайными числами')
flag = 0
choice = 0
while True:
    if choice != '2': choice = input()
    if choice.isnumeric():
        if int(choice) == 1:
            f = open('1.txt','r')
            rows = 0
            for x in range(N):
                s = f.readline().split()
                if s == []:
                    break
                for y in range(N):
                    A[x][y] = int(s[y])
                    F[x][y] = A[x][y]
                rows += 1
            print('Вы заполнили матрицу А из файла.')
            break
        elif int(choice) == 2:
                print('Вы заполнили матрицу случайными числами от -10 до 10.')
                for x in range(N):
                    for y in range(N):
                        A[x][y] = randint(-10,10)
                        F[x][y] = A[x][y]
                break
        else: print('Введено неверное число. Ответом на вопрос должно быть число:\n 1 - из файла 2 - случайными числами')
    else: print('Ответом на вопрос должно быть целое число:\n 1 - из файла 2 - случайными числами')
ch=0
if N%2==0: ch=1
count = 0
for x in range(N//2-ch):#область 2
    for y in range(1,N-x-1):
            if (y+1)%2 == 0 and F[x][y]>K: count += 1
print(f'Количество чисел, больших {K} в четных столбцах во 2 области равно {count}.')
mult = 1
nch=0
for x in range(N//2+nch,N):#область 4
    for y in range(1,N-x-1):
        if (x+1)%2!=0: mult*=F[x][y]
print(f'Произведение чисел в нечетных строках области 4 равно {mult}.')
if count > mult:
    for x in range(1,N-1):
        for y in range(x):
            if y < (N-1-x): F[x][y], F[N-1-y][N-1-x] = F[N-1-y][N-1-x], F[x][y]
    print('Матрица F была изменена симметрично.')
else:
    for x in range(1,N-1):
        for y in range(x):
                if y < (N-1-x): F[x][y], F[N-1-y][x] = F[N-1-y][x], F[x][y]
    print('Матрица F была изменена несимметрично.')
print(f'\nПервоначальная матрица А:')
for x in range(N):
    for y in range(N): 
        print(A[x][y], end = ' ')
    print()
print(f'\nПервоначальная матрица F:') 
for x in range(N):
    for y in range(N): 
        print(F[x][y], end = ' ')   
    print()
print(f'\nМатрица F, перемноженная с матрицей А:')
for x in range(N):    
    for y in range(N):
        for i in range(N): prom += F[x][i] * A[i][y]
        A[x][y], prom = prom, 0
        print(A[x][y], end = ' ')
    print()   
print(f'\nМатрица F, перемноженная с матрицей А, умноженная на {K}:')
for x in range(N):
    for y in range(N):
        A[x][y] *= K
        print(A[x][y], end = ' ')
    print()
print('\nТранспортированная матрица F:')
for x in range(N):
    for y in range(x): 
        F[x][y], F[y][x] = F[y][x], F[x][y]
for x in range(N):
    for y in range(N): print(F[x][y], end = ' ')
    print()
print(f'\nТранспортированная матрица F, умноженная на {K}:')
for x in range(N):
    for y in range(N):
        F[x][y] *= K
        print(F[x][y], end = ' ')
    print()
print('\nРезультат операции К*(A*F) + K*Ft:')
for x in range(N):    
    for y in range(N):
        F[x][y] += A[x][y]
        print(F[x][y], end = ' ')
    print()