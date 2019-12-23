from math import gcd
import tqdm

szukane = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289}
correct_numbers = []
correct_sums = []


def count_sums_compr():
    return [x + y for x in tqdm.tqdm(correct_numbers) for y in correct_numbers if x + y < 314]


def count_sums_loops():
    sums = []
    for number in tqdm.tqdm(correct_numbers):
        for number2 in correct_numbers:
            if number + number2 < 314:
                sums.append(number + number2)
    return sums


with open('lista_kodow.txt', 'r') as kody_plik:
    kody = kody_plik.read().splitlines()

for kod in tqdm.tqdm(kody):
    if int(kod[:2]) + int(kod[3:]) < 314:
        correct_numbers.append(int(kod[:2]) + int(kod[3:]))

print("Ilość spełniająca warunek: {}".format(correct_numbers.__len__()))

correct_sums = count_sums_loops()

print("Ilość poprawnych sum: {}".format(correct_sums.__len__()))

spelniajace_warunek = 0

for suma in tqdm.tqdm(correct_sums):
    if 314 - suma in szukane:
        spelniajace_warunek += 1

print("Ilość spełniająca równanie: {}".format(spelniajace_warunek))
wszystkie = kody.__len__() ** 2

print(wszystkie)
print(spelniajace_warunek / wszystkie)
print(kody.__len__())

corr_compr = count_sums_compr()

print(correct_sums == corr_compr)

# import timeit
#
# print(timeit.timeit('count_sums_loops()', setup='from __main__ import count_sums_loops', number=100))
# print(timeit.timeit('count_sums_compr()', setup='from __main__ import count_sums_compr', number=100))
