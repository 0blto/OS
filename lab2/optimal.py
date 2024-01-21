import math

from prettytable import PrettyTable


# FIFO
def manage(pages, shots_number):
    replaces_number = 0
    output = PrettyTable()
    field_names = ['shot ' + str(i + 1) for i in range(shots_number)]
    output.field_names = field_names
    state = []
    optimal = dict()
    for i in range(len(pages)):
        if not pages[i] in optimal.keys(): optimal[pages[i]] = [i]
        else: optimal[pages[i]].append(i)
    for i in range(len(pages)):
        optimal[pages[i]].pop(0)
        if i != 0: output.add_row(state + [0] * (shots_number - len(state)))
        if pages[i] in state: continue
        if len(state) < shots_number: state.append(pages[i]); continue
        replaces_number += 1
        replace_index = 0
        next_usage = optimal[state[0]][0] if optimal[state[0]] else math.inf
        for j in range(len(state)):
            if not optimal[state[j]]:
                replace_index = j
                next_usage = math.inf
                break
            if optimal[state[j]][0] > next_usage:
                replace_index = j
                next_usage = optimal[state[j]][0]
        state[replace_index] = pages[i]
    output.add_row(state)
    return {'table': output, 'replaces': replaces_number}
