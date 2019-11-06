'''

B-5 N面サイコロ

'''
import random

dice_faces = int(input('\nサイコロの面の数は?: '))
num_roll = int(input('何回振りますか?: '))

#連番を作る https://pg-chain.com/python-range
dice_numer_list = list(range(1, dice_faces+1))

# for文繰り返す回数 https://www.javadrive.jp/python/for/index5.html
def dice_rolling():
    list = []
    for i in range(num_roll):
        list.append(random.choice(dice_numer_list))
    print()
    print(f'サイコロの目は {list}')

dice_rolling()
