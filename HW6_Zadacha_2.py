#2. Задайте натуральное число N. Напишите программу, которая составит
#  список простых множителей числа N.
n = int(input("Задайте натуральное число "))

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

a = list(filter(lambda val: is_prime(val) and n % val==0, list(range(2,n))))

print(a)