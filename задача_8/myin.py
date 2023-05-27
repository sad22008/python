# 3 2 4 -> yes
# 3 2 1 -> no'''

n = int(input("Введите размер шоколадки n "))
m = int(input("Введите размер шоколадки m "))
k = int(input("Введите количество долек k "))

if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')