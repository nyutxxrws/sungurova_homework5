import random
import math
import statistics
numbers = [random.randint(1, 100) for i in range(100)]
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
stdev_value = statistics.stdev(numbers)
sum_numbers = sum(numbers)
sqrt_sum = round(math.sqrt(sum_numbers), 2)
print(f"Среднее: {mean_value:.2f}, "
      f"Медиана: {median_value}, "
      f"Стандартное отклонение: {stdev_value:.2f}, "
      f"Корень из суммы: {sqrt_sum}")
