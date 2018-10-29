import time

# print(time.gmtime(0))
# print(time.localtime()) # same as below
# print(time.localtime(time.time()))
#
# print(time.time())
#
# time_here = time.localtime()
# print(time_here)
# print("year:", time_here[0], time_here.tm_year)
# print('month:', time_here[1], time_here.tm_mon)
# print('day:', time_here[2], time_here.tm_mday)

from time import perf_counter as my_timer
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")
end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))

print("ur reaction was {} seks".format(end_time - start_time))
