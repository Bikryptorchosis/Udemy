from time import get_clock_info as info

print(info('time'))
print(info('monotonic'))
print(info('perf_counter'))
print(info('process_time'))


print("time():\t\t\t", info('time'))
print("monotonic():\t", info('monotonic'))
print("perf_counter():\t", info('perf_counter'))
print("process_time():\t", info('process_time'))
