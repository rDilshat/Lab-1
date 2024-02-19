from datetime import datetime
def calculation(date1, date2):
    date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    dif = date2 - date1
    deltaseconds = dif.total_seconds()
    return deltaseconds
date1 = '2024-02-18 17:24:30'
date2 = '2024-02-18 17:24:52'
print(calculation(date1, date2))