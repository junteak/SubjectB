'''

B5 基本統計量の計算

'''




print('基本統計量の計算')



#スペースで区切ってリスト nums = [int(e) for e in input().split()]  https://teratail.com/questions/151229
nums = [int(e) for e in input('Enter several numbers to statistics by seperating with spaces : ').split()]
print(nums)

#sumを使わない合計 https://www.atmarkit.co.jp/ait/articles/1906/11/news007.html
def sum():
    sum_add = 0
    for num in nums:
        sum_add = sum_add + num
    print(f'Total: {sum_add}')
sum()

#sumを使わない最大値 https://codeday.me/jp/qa/20190313/399952.html
def max():
    max_add = 0
    for num in nums:
        if num > max_add:
            max_add = num
    print(f'Max: {max_add}')
max()

def min():
    min_add = nums[0]
    for num in nums:
        if num < min_add:
            min_add = num
    print(f'Min: {min_add}')
min()

def ave():
    ave_add = 0
    for num in nums:
        ave_add += num
    print(f'Min: {int(ave_add/len(nums))}')
ave()

