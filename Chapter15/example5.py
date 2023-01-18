from random import randint
import time

start = time.perf_counter()

def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

data = []
for i in range(10000):
    data.append(randint(0, 100))

bubbleSort(data)
end = time.perf_counter()
print(end-start)
temp = input()