#3. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д
nums = list(map(int, input("Введите числа ").split()))
n = len(nums) // 2 + len(nums) % 2
for i,j in zip(nums[:n], nums[-1:-n - 1:-1]):
    print(i*j)