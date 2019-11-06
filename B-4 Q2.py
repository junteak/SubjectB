'''

課題 B-4 Q2

'''

print('\nSubject B4 Q2, Station Names of Osaka\n')

weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]



# 1.最初にやったやつ
# def osaka_st():
#     list_Osaka = list()
#     for osaka_i in range(3, 6):
#         list_Osaka.append(weather_information[osaka_i]['station'])
#     return f'{list_Osaka[0]},{list_Osaka[1]},{list_Osaka[2]}'
#
# print(osaka_st())


# 2．次にやったやつ
# # print(f'{weather_information[3]["station"]},{weather_information[4]["station"]},{weather_information[5]["station"]}')


# 3.．みつけた関数 join()
def osaka_st():
    list_Osaka = []
    for osaka_i in range(3, 6):
        list_Osaka.append(weather_information[osaka_i]['station'])
    print(','.join(list_Osaka))

osaka_st()