import pandas as pd

dt = pd.read_csv("data.csv", delimiter=';', names=['Data', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1'], index_col=0)
dt['srednee'] = (dt['10'] + dt['9'] + dt['8'] + dt['7'] + dt['6'] + dt['5'] + dt['4'] + dt['3'] + dt['2'] + dt['1'])/10 #вычисляем среднюю температуру
dt['so'] = dt.std(axis=1, numeric_only=True) #вычисляем среднеквадратическое отклонение по строчно

enter_data_day = int(input('Введите день месяца: '))
print('Данные за последние 9 лет на', enter_data_day, 'число нынешнего месяца.')
print(dt['srednee'][enter_data_day], '- средняя температура.')
print(dt['so'][enter_data_day], '- среднеквадратическое отклонение.')