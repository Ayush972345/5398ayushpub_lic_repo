import time
dict = {}
list1 = {12,43,56}
list2 = {"ag", "ds", "we"}

for i,j in zip(list1, list2):
    dict[i] = j

for i in range(10):
    print(dict)
    time.sleep(2)