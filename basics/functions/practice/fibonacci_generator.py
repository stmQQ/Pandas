import itertools


def fibonacci_generator(limit=None, filter_func=None):
    """
    Генератор чисел Фибоначчи с фильтрацией
    limit: максимальное количество чисел (None - бесконечно)
    filter_func: функция-фильтр (None - без фильтра)
    """
    a, b = 0, 1
    count = 0
    cache = []
    while limit is None or count < limit:
        if count < len(cache):
            current = cache[count]
        else:
            current = a
            cache.append(current)
            a, b = b, a + b
        
        if filter_func is None or filter_func(current):
            yield current
            count += 1
        


# 1. Первые 10 чисел Фибоначчи
print("Первые 10:", list(fibonacci_generator(10)))

# 2. Только четные числа (первые 5)
even_filter = lambda x: x % 2 == 0
print("Четные:", list(fibonacci_generator(5, even_filter)))

# 3. Числа > 100 (первые 3)
large_filter = lambda x: x > 100
print("Больше 100:", list(fibonacci_generator(3, large_filter)))

# 4. Бесконечный генератор (взять 15)
gen = fibonacci_generator()
first_15 = list(itertools.islice(gen, 15))
print("Первые 15:", first_15)

# 5. Числа, делящиеся на 5 (первые 4)
div_by_5 = lambda x: x % 5 == 0 and x != 0
print("Делятся на 5:", list(fibonacci_generator(4, div_by_5)))