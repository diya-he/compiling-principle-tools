import json

def init_states(fa):
    for i in list(range(fa.num_states)):
        fa.states.append(str(i))

def construct_from_file(fa, filepath):
    nfa_json = json.load(open(filepath, 'r', encoding="utf-8"))
    fa.num_states  = nfa_json['num_states']
    init_states(fa)
    fa.symbols = nfa_json['symbols']
    fa.end_states = nfa_json['end_states']
    fa.start_states = nfa_json['start_states']
    transition = nfa_json['transition_functions']
    for t in transition:
        transition_function = (t[0], t[1], t[2])
        fa.transition_functions.append(transition_function)

def print_fa(fa):
    print('节点数量：', fa.num_states)
    print('节点', fa.states)
    print('路径', fa.symbols)
    print('终止状态', fa.end_states)
    print('起始状态', fa.start_states)
    print('转化路径', fa.transition_functions)


def simple_state_fa(fa):
    mapping_table = {}
    for i in range(len(fa.states)):
        mapping_table[str(fa.states[i])] = str(i)
    print(mapping_table)
    for i in range(len(fa.end_states)):
        fa.end_states[i] = mapping_table[str(fa.end_states[i])]
    for i in range(len(fa.start_states)):
        fa.start_states[i] = mapping_table[str(fa.start_states[i])]
    new_transition = []
    for transition in (fa.transition_functions):
        tup = (mapping_table[str(transition[0])], transition[1], mapping_table[str(transition[2])])
        new_transition.append(tup)
    fa.transition_functions = new_transition

    for i in range(len(fa.states)):
        fa.states[i] = mapping_table[str(fa.states[i])]


def save_fa_to_json(fa, filepath):
    # simple_state_fa(fa)
    dict = {
        "num_states": fa.num_states,
        "symbols": fa.symbols,
        "end_states": fa.end_states,
        "start_states": fa.start_states,
        "transition_functions": fa.transition_functions
    }
    with open(filepath, "w") as json_file:
        json_dict = json.dump(dict, json_file)

