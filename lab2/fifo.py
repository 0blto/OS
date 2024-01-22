from prettytable import PrettyTable


# FIFO
def manage(pages, shots_number):
    replaces_number = 0
    output = PrettyTable()
    field_names = ['кадр ' + str(i + 1) for i in range(shots_number)]
    output.field_names = field_names
    state = []
    fifo = [i for i in range(shots_number)]
    for i in range(len(pages)):
        if i != 0: output.add_row(state + [''] * (shots_number - len(state)))
        if pages[i] in state: continue
        if len(state) < shots_number: state.append(pages[i]); continue
        replaces_number += 1
        fifo.append(fifo.pop(0))
        state[fifo[-1]] = pages[i]
    output.add_row(state)
    return {'table': output, 'replaces': replaces_number}
