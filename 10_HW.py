
import pandas as pd
import random

lst = ['robot'] * 10  # копирует 10 раз robot в массиве
lst += ['human'] * 10  # копирует 10 раз human в массиве и добавляет его к robot

random.shuffle(lst)  # перемешивает эл-ты в массиве
data = pd.DataFrame({'whoAmI': lst})  # создает dataframe
print(data.head())  # вывод первых 5 строк

print()

data = pd.get_dummies(data['whoAmI'], dtype=int)
print(data.head())





