
print('\nkuku_3\n')


row = int(input('Enter the number of rows: '))
column = int(input('Enter the number of columns: '))

for a in range(1, row + 1):
    for b in range(1, column + 1):
        print('{}×{}= {}| '.format(a, b, a*b), end=" ")
    print()

