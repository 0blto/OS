import math
from prettytable import PrettyTable


# LRU
def manage(pages, shots_number):
    replaces_number = 0
    system_time = 0
    output = PrettyTable()
    field_names = ['кадр ' + str(i + 1) for i in range(shots_number)]
    output.field_names = field_names
    state = []
    lru = dict()
    for i in set(pages): lru[i] = math.inf
    for i in range(len(pages)):
        system_time += 1
        lru[pages[i]] = system_time
        if i != 0: output.add_row(state + [''] * (shots_number - len(state)))
        if pages[i] in state: continue
        if len(state) < shots_number: state.append(pages[i]); continue
        replaces_number += 1
        remove_index = 0
        lru_time = lru[state[remove_index]]
        for j in range(1, len(state)):
            if lru[state[j]] < lru_time:
                lru_time = lru[state[j]]
                remove_index = j
        state[remove_index] = pages[i]
    output.add_row(state)
    return {'table': output, 'replaces': replaces_number}
