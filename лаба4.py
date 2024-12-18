lst = list(map(int, input("Введите элементы списка через пробел: ").split()))

if not all(isinstance(x, int) for x in lst): #Проверка корректности вводимых данных
    print("Ошибка: Введите только целочисленные значения.")
    quit()

print("Список:", lst)

last_element = lst[-1]
sum_greater_than_last = sum(x for x in lst if x > last_element)
print("Сумма элементов списка, больших последнего элемента:", sum_greater_than_last)

max_abs_element_index = max(range(len(lst)), key=lambda i: abs(lst[i]))
product_before_max_abs = 1
for i in range(max_abs_element_index):
    product_before_max_abs *= lst[i]
print("Произведение элементов списка, расположенных до максимального по модулю элемента:", product_before_max_abs)
