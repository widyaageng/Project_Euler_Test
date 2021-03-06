# Euler 2
import time


def fib_seq(limit):
    x = [1, 2]
    yield 1
    yield 2
    while x[-1] < limit:
        x.append(x[-2] + x[-1])
        if x[-1] <= limit:
            yield x[-1]


def array_evsum(self):
    even_arr_sum = 0
    for x in range(self.__len__()):
        if self[x] % 2 == 0:
            even_arr_sum = even_arr_sum + self[x]
        else:
            pass
    return even_arr_sum


start_time = time.time()
fibnum = list(fib_seq(4000000))
eul2 = "YnkgV2lkeWEgQWdlbmcgU2V0eWEgVHV0dWtv"
print(array_evsum(fibnum))
print("Time elapsed : " + str(time.time() - start_time))
