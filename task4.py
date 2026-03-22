import random
from datetime import date, timedelta
from array import array
current_date = date.today()
dates = []
differences = array('i')
for n in range(10):
    random_date = current_date - timedelta(days=random.randint(0, 1825))
    dates.append(random_date)
for i in range(len(dates) - 1):
    diff = abs((dates[i] - dates[i+1]).days)
    differences.append(diff)
    print(f"Разница между {dates[i]} и {dates[i+1]}: {diff} дней")
