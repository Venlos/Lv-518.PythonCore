n = int(input("Введите число:"))
str1=str(n)

mult = 1
while n > 0:
    digit = n % 10
    mult = mult * digit
    n = n // 10
print("Произведение:", mult)
print("Реверс:", str1[::-1])
print("Сортировка:",sorted(str1))

