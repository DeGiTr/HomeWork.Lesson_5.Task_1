# Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "положительное нечетное число", 
# например, численным описанием числа 190 является строка "положительное четное число". Если число не является четным - выведите сообщение "число не является четным"

print("Давате узнаем вид числа!")
num = int(input("Введите число: "))

if (num > 0) and (num % 2 == 0):
    print("Положительное четное число")
elif (num > 0) and (num % 2 != 0):
    print("Положительное нечетное число")
elif (num < 0) and (num % 2 == 0):
    print("Отрицательное четное число")
elif (num < 0) and (num % 2 != 0):
    print("Отрицательное нечетное число")
else:
    print("Нулевое число")