# Скачать файл titanic.csv https://drive.google.com/file/d/1UPLPuINv0EqZzJJcg1c48_FfdIynDPIr/view?usp=sharing
#
# Все задания будут происходить над датафреймом заргуженным так:
import pandas

df = pandas.read_csv('titanic.csv')

#
#
# Описание таблицы
# Name - имя
# Sex - пол 'male' | 'female'
# Age - возраст
# Pclass - социоэкономический статус:
#  1 абрамович
#  2 хватило на timberland
#  3 нищеброд
# Survived - выжил 1 или нет 0
#
#
# 1. Распечатайте колонки которые есть датафрейме.
print(df.columns)
# print(df.head())

# 2. Узнайте сколько людей было на борту
print('--------количество людей на борту')
print(df.count())

# 3. Узнайте сколько на борту было мужчин.
print('--------выжили по полу и полю имени')
print(df.groupby(['Sex', 'Survived'])['Name'].count())
print('--------выжили по полу и всем полям')
print(df.groupby(['Sex', 'Survived']).count())

# 4. Посчитайте процент выживших на борту.
#
print('--------процент выживших')
cnt = df.groupby(['Survived'])['Name'].count().sum()
print('--------число выживших', cnt)
print(df.groupby(['Survived'])['Name'].count())
print(df.groupby(['Survived'])['Name'].count() / cnt * 100)

# 5. Кого было больше на борту, мужчин или женщин ?
print('--------по полу')
print(df.groupby(['Sex'])['Name'].count())

# 6. Посчитайте сколько процентов из выживших были мужчинами?
print('--------число выживших по полу')
print(df.groupby(['Sex', 'Survived'])['Name'].count() / cnt * 100)
# 7. Человек какого класса вероятнее всего не выжил ?
#
print('--------по классу')
print(df.groupby(['Pclass', 'Survived'])['Name'].count())
print('--------по классу процент')
print(df.groupby(['Pclass', 'Survived'])['Name'].count() / cnt * 100)
