import lru
import fifo
import optimal

# HEEE'S BAAACK

SHOTS_NUMBER = 4
EXTENDED_SHOTS_NUMBER = SHOTS_NUMBER * 2
REDUCED_SHOTS_NUMBER = SHOTS_NUMBER // 2
pages = [20, 10, 1, 12, 20, 1, 13, 2, 7, 15, 5, 9, 6, 11, 7, 3, 13, 8, 2, 22, 19, 21, 7, 5, 17,
    19, 2, 19, 13, 15, 14, 1, 6, 15, 22, 21, 22, 8, 1, 22, 16, 12, 18, 6, 10, 7]

fifo_default = fifo.manage(pages, SHOTS_NUMBER)
fifo_extended = fifo.manage(pages, EXTENDED_SHOTS_NUMBER)
fifo_reduced = fifo.manage(pages, REDUCED_SHOTS_NUMBER)

lru_default = lru.manage(pages, SHOTS_NUMBER)
lru_extended = lru.manage(pages, EXTENDED_SHOTS_NUMBER)
lru_reduced = lru.manage(pages, REDUCED_SHOTS_NUMBER)

optimal_default = optimal.manage(pages, SHOTS_NUMBER)
optimal_extended = optimal.manage(pages, EXTENDED_SHOTS_NUMBER)
optimal_reduced = optimal.manage(pages, REDUCED_SHOTS_NUMBER)

print('FIFO\n')
print(fifo_default['table'])
print('\n')
print('Replaces number: ', fifo_default['replaces'])
print('Replaces number with //2 shots: ', fifo_reduced['replaces'])
print('Replaces number with x2 shots: ', fifo_extended['replaces'])
print('\n')

print('LRU\n')
print(lru_default['table'])
print('\n')
print('Replaces number: ', lru_default['replaces'])
print('Replaces number with //2 shots: ', lru_reduced['replaces'])
print('Replaces number with x2 shots: ', lru_extended['replaces'])
print('\n')

print('OPTIMAL\n')
print(optimal_default['table'])
print('\n')
print('Replaces number: ', optimal_default['replaces'])
print('Replaces number with //2 shots: ', optimal_reduced['replaces'])
print('Replaces number with x2 shots: ', optimal_extended['replaces'])
print('\n')

total_requests = len(pages)
print('Reducing cache misses to 5% with optimal algorithm')
print('Total requests pages: ', total_requests)
for i in range(2, len(pages)):
    current_percent = optimal.manage(pages, i)['replaces']/total_requests*100
    print("Cash misses percent with {0} shots: {1:2.2f}%".format(i, current_percent))
    if current_percent <= 5: break
