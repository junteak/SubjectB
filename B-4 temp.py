'''

課題 B4 Q1

'''

print('\nSubject B-4, Temparature\n')

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

# なぜできないのかわからなかったやつ
# for a in weather_information[range(0,7)]['temrpareture']:
#         print(a)


def calculate_average():
        list_temperature = []
        for i in range(0, 8):
                list_temperature.append(weather_information[i]['temperature'])
        return sum(list_temperature) / 8

print(f'全国の平均気温は{calculate_average()}度')
