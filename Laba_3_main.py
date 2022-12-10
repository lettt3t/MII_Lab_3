import csv
import random
import statistics
import numpy
import pandas
import matplotlib.pyplot as plt

def read_file(file):
    ret_list = []
    f = open(file,encoding="utf-8")
    for line in f.read().splitlines():
        ret_list.append(line)
    return ret_list

surnames_male = read_file("fio_male.txt")
surnames_female = read_file("fio_famale.txt")
posts = read_file("dolz.txt")
Data_list = []

with open("array_list.csv", "w") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\r")
    writer.writerow(
        ["Табельный номер", "Фамилия", "Пол", "Год рождения", "Год начала работы в компании", "Подразделение",
         "Должность", "Оклад", "Кол-во выполненных проектов"])
    for i in range(1, 1100):
        temp_sex = random.randint(0, 1)
        temp_birthyear = random.randint(1970, 1990)
        temp_startwork = random.randint(temp_birthyear + random.randint(18, 31), 2022)
        temp_post = random.choice(posts)
        temp_subdiv = random.randint(1, 5)
        ye_of_work = 2022 - temp_startwork
        if ye_of_work < 5:
            temp_projects = random.randint(1, 30)
        elif ye_of_work > 5:
            temp_projects = random.randint(30, 100)

        if ye_of_work == 1:
            temp_salary = random.randrange(20000, 25000, 1000) + temp_projects * 100
        elif ye_of_work < 5:
            temp_salary = random.randrange(20000, 25000, 1000) + temp_projects * 100
        elif ye_of_work < 7:
            temp_salary = random.randrange(25000, 30000, 1000) + temp_projects * 100
        elif ye_of_work > 7:
            temp_salary = random.randrange(30000, 35000, 1000) + temp_projects * 100
        temp_id = i
        if temp_sex == 0:
            sex_str = "Мужской"
            temp_surname = random.choice(surnames_male)
        elif temp_sex == 1:
            sex_str = "Женский"
            temp_surname = random.choice(surnames_female)
        writer.writerow(
            [temp_id, temp_surname, sex_str, temp_birthyear, temp_startwork, temp_subdiv,
             temp_post, temp_salary, temp_projects])

new_list = []
with open("array_list.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        new_list.append(row)

header_1 = headers[3]
data = []

for cell in new_list:
    data.append(int(cell[3]))

stat_array_1 = numpy.array(data)
print("\nNumpy_1")
print("Статистические данные для столбца \"%s\" " % header_1)
print("Минимальное значение:", numpy.min(stat_array_1))
print("Максимальное значение:", numpy.max(stat_array_1))
print("Среднее значение:", numpy.average(stat_array_1))
print("Дисперсия:", numpy.var(stat_array_1))
print("Стандартное отклонение:", numpy.std(stat_array_1))
print("Медиана:", numpy.median(stat_array_1))
print("Мода:", statistics.mode(stat_array_1))
print("\n")

header_2 = headers[8]
data = []

for cell in new_list:
    data.append(int(cell[8]))

stat_array_2 = numpy.array(data)
print("\nNumpy_2")
print("Статистические данные для столбца \"%s\" " % header_2)
print("Минимальное значение:", numpy.min(stat_array_2))
print("Максимальное значение:", numpy.max(stat_array_2))
print("Среднее значение:", numpy.average(stat_array_2))
print("Дисперсия:", numpy.var(stat_array_2))
print("Стандартное отклонение:", numpy.std(stat_array_2))
print("Медиана:", numpy.median(stat_array_2))
print("Мода:", statistics.mode(stat_array_2))
print("\n")

header_3 = headers[7]
data = []

for cell in new_list:
    data.append(int(cell[7]))

stat_array_3 = numpy.array(data)
print("\nNumpy_3")
print("Статистические данные для столбца \"%s\" " % header_3)
print("Минимальное значение:", numpy.min(stat_array_3))
print("Максимальное значение:", numpy.max(stat_array_3))
print("Среднее значение:", numpy.average(stat_array_3))
print("Дисперсия:", numpy.var(stat_array_3))
print("Стандартное отклонение:", numpy.std(stat_array_3))
print("Медиана:", numpy.median(stat_array_3))
print("Мода:", statistics.mode(stat_array_3))
print("\n")

df_stat = pandas.read_csv("array_list.csv", header=0, index_col=0, encoding="cp1251")
print("\npandas_1:")
print("Статистические данные для столбца \"%s\" " % "Год рождения")
print("Минимальное значение:", df_stat["Год рождения"].min())
print("Максимальное значение:", df_stat["Год рождения"].max())
print("Среднее значение:", df_stat["Год рождения"].mean())
print("Дисперсия:", df_stat["Год рождения"].var())
print("Стандартное отклонение:", df_stat["Год рождения"].std())
print("Медиана:", df_stat["Год рождения"].median())
print("Мода:", df_stat["Год рождения"].mode())

print("\npandas_2:")
print("Статистические данные для столбца \"%s\" " % "Оклад")
print("Минимальное значение:", df_stat["Оклад"].min())
print("Максимальное значение:", df_stat["Оклад"].max())
print("Среднее значение:", df_stat["Оклад"].mean())
print("Дисперсия:", df_stat["Оклад"].var())
print("Стандартное отклонение:", df_stat["Оклад"].std())
print("Медиана:", df_stat["Оклад"].median())
print("Мода:", df_stat["Оклад"].mode())

print("\npandas_3:")
print("Статистические данные для столбца \"%s\" " % "Кол-во выполненных проектов")
print("Минимальное значение:", df_stat["Кол-во выполненных проектов"].min())
print("Максимальное значение:", df_stat["Кол-во выполненных проектов"].max())
print("Среднее значение:", df_stat["Кол-во выполненных проектов"].mean())
print("Дисперсия:", df_stat["Кол-во выполненных проектов"].var())
print("Стандартное отклонение:", df_stat["Кол-во выполненных проектов"].std())
print("Медиана:", df_stat["Кол-во выполненных проектов"].median())
print("Мода:", df_stat["Кол-во выполненных проектов"].mode())

plt.figure()
plt.subplot(2, 2, 1)
plt.title("Оклад")
plt.xlabel("Год начала работы в компании")
plt.ylabel("Оклад")
plt.plot(df_stat["Год начала работы в компании"].sort_values(), df_stat["Оклад"].sort_values())

plt.subplot(2, 2, 2)
plt.title("Оклад")
plt.xlabel("Количество выполненных проектов")
plt.ylabel("Оклад")
plt.plot(df_stat["Кол-во выполненных проектов"].sort_values(), df_stat["Оклад"].sort_values())

plt.subplot(2, 2, 3)
plt.title("Пол сотрудников")
labels = "Женщины", "Мужчины"
male_count = 0
female_count = 0
for sex in df_stat["Пол"]:
    if sex == "Мужской":
        male_count = male_count + 1
    elif sex == "Женский":
        female_count = female_count + 1
sizes = [female_count, male_count]
explode = (0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)


plt.subplot(2,2,4)
plt.bar(labels, sizes)
plt.show()

