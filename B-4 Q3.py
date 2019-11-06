'''

課題 B-4 Q3

'''

print('\nSubject B4 Q3, Average of Fukuoka\n')

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


def ave_f_temp():
    list_f_temp = [weather_information[6]['temperature'],weather_information[7]['temperature']]
    ave = sum(list_f_temp) / len(list_f_temp)
    print(f'福岡の平均気温は{ave}度')

ave_f_temp()