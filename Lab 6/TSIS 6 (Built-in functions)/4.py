import time
def calculator(num, waittime):
    time.sleep(waittime * 0.001)
    return num**0.5
num = 25100
t = 2123
res = calculator(num, t)
print(f"Square root of {num} after {t} miliseconds is {res}")