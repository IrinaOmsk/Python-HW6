#1. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
nums = list(map(float, input("Введите числа ").split()))
lst = list(filter(lambda val: val != 0, map(lambda val: val-int(val), nums)))

print(max(lst)- min(lst))