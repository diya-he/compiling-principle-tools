import json

class NFA:
    def __init__(self):
        self.num_states = 0
        self.states = []
        self.symbols = []
        self.end_states = []
        self.start_states = []
        self.transition_functions = []


    def init_states(self):
        for i in list(range(self.num_states)):
            self.states.append(str(i))


    def print_nfa(self):
        print(self.num_states)
        print(self.states)
        print(self.symbols)
        print(self.end_states)
        print(self.start_states)
        print(self.transition_functions)

    def e_closure(self, state_table):
        for state in state_table:
            for trans in self.transition_functions:
                if state == trans[0] and trans[1] == '$':
                    state_table.append(trans[2])
        return state_table

    def construct_nfa_from_file(self, lines, filepath):
        nfa_json = json.load(open(filepath, 'r', encoding="utf-8"))
        self.num_states = nfa_json['num_states']
        for i in range(self.num_states):
            self.states.append(str(i))
        self.symbols = nfa_json['symbols']
        self.end_states = nfa_json['end_states']
        self.start_states = nfa_json['start_states']
        transition = nfa_json['transition_functions']
        for t in transition:
            transition_function = (t[0], t[1], t[2])
            self.transition_functions.append(transition_function)


class DFA:
    def __init__(self):
        self.num_states = 0
        self.states = []
        self.symbols = []
        self.end_states = []
        self.start_states = []
        self.transition_functions = []

    def construct_dfa_from_file(self, lines, filepath):
        nfa_json = json.load(open(filepath, 'r', encoding="utf-8"))
        self.num_states = nfa_json['num_states']
        for i in range(self.num_states):
            self.states.append(str(i))
        self.symbols = nfa_json['symbols']
        self.end_states = nfa_json['end_states']
        self.start_states = nfa_json['start_states']
        transition = nfa_json['transition_functions']
        for t in transition:
            transition_function = (t[0], t[1], t[2])
            self.transition_functions.append(transition_function)

    def convert_from_nfa(self, nfa):
        self.symbols = nfa.symbols
        start_dfa = nfa.start_states
        #求初始节点的空闭包
        start_dfa = nfa.e_closure(start_dfa)
        self.states.append(start_dfa)
        for state in self.states:#状态
            for symbol in self.symbols:#路径标志
                state_symbol = []
                #当前路径的下个新状态
                for s in state:
                    for trans in nfa.transition_functions:
                        if s == trans[0] and symbol == trans[1]:
                            state_symbol.append(trans[2])
                #求空闭包
                state_symbol = nfa.e_closure(state_symbol)
                state_symbol = list(set(state_symbol))
                if state_symbol != []:
                    # 放入transition_functions
                    transition = (state, symbol, state_symbol)
                    self.transition_functions.append(transition)

                    # 更新states
                    for s in self.states:
                        if s == state_symbol:
                            break
                        elif s == self.states[len(self.states) - 1] and s != state_symbol:
                            self.states.append(state_symbol)

        self.num_states = len(self.states)

        for state in self.states:
            for s1 in nfa.end_states:
                for s in state:
                    if s == s1 and state not in self.end_states:
                        self.end_states.append(state)
                        break

        for state in self.states:
            for s1 in nfa.start_states:
                for s in state:
                    if s == s1 and state not in self.start_states:
                        self.start_states.append(state)
                        break


    def print_dfa(self):
        print('节点数量：', self.num_states)
        print('节点', self.states)
        print('路径', self.symbols)
        print('终止状态', self.end_states)
        print('起始状态', self.start_states)
        print('转化路径', self.transition_functions)


    def simple_state_dfa(self):
        state_0_ = self.states[0]
        state_1_ = self.states[1]
        state_2_ = self.states[2]
        index = 0
        for s in self.states:
            if s == state_0_:
                self.states[index] = '0'
            elif s == state_1_:
                self.states[index] = '1'
            elif s == state_2_:
                self.states[index] = '2'
            index = index + 1
        index = 0
        for s in self.end_states:
            if s == state_0_:
                self.end_states[index] = '0'
            elif s == state_1_:
                self.end_states[index] = '1'
            elif s == state_2_:
                self.end_states[index] = '2'
            index = index + 1
        index = 0
        for s in self.start_states:
            if s == state_0_:
                self.start_states[index] = '0'
            elif s == state_1_:
                self.start_states[index] = '1'
            elif s == state_2_:
                self.start_states[index] = '2'
            index = index + 1
        index = 0
        for t in self.transition_functions:
            temple = []
            if t[0] == state_0_:
                temple.append('0')
            elif t[0] == state_1_:
                temple.append('1')
            elif t[0] == state_2_:
                temple.append('2')
            temple.append(t[1])
            if t[2] == state_0_:
                temple.append('0')
            elif t[2] == state_1_:
                temple.append('1')
            elif t[2] == state_2_:
                temple.append('2')
            self.transition_functions[index] = tuple(temple)
            index = index + 1

    def save_dfa_json(self, filepath):
        self.simple_state_dfa()
        dict = {
            "num_states": self.num_states,
            "symbols": self.symbols,
            "end_states": self.end_states,
            "start_states": self.start_states,
            "transition_functions": self.transition_functions
        }
        with open(filepath, "w") as json_file:
            json_dict = json.dump(dict, json_file)
