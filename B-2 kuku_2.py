
print('\nkuku_2\n')

row = int(input('行数を入力してください: '))
column = int(input('列数を入力してください: '))

for a in range(1, row + 1):
    for b in range(1, column + 1):
        print(a*b, end=" ")
    print()

