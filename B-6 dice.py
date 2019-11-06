'''

B-5 N面サイコロ

'''
import random


dice_faces = int(input('\nHow many are the dice faces?: '))
num_roll = int(input('How many times do I roll the dice?: '))

#連番を作る https://pg-chain.com/python-range
dice_numer_list = list(range(1, dice_faces+1))

# for文繰り返す回数 https://www.javadrive.jp/python/for/index5.html
def dice_rolling():
    list = []
    for i in range(num_roll):
        list.append(random.choice(dice_numer_list))
    print()
    print(f'The pip of the dice is {list}')

dice_rolling()
