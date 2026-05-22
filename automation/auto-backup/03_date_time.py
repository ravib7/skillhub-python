from datetime import datetime

# result = datetime.datetime.now()
result = datetime.now()                           
year = datetime.now().strftime("%Y") # date-fns
month = datetime.now().strftime("%m")
day = datetime.now().strftime("%d")

hours = datetime.now().strftime("%H")
min = datetime.now().strftime("%M")
sec = datetime.now().strftime("%S")
s = f"{day}-{month}-{year}_{hours}-{min}-{sec}"
fs = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

print(result)
print(year, month, day)
print(hours, min, sec)
print(s)
print(fs)
