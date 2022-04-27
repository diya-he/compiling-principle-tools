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


    def construct_nfa_from_file(self, lines):
        self.num_states = int(lines[0])
        self.init_states() #0,1,2
        self.symbols = list(lines[1].strip())

        end_states_line = lines[2].split(" ")
        for index in range(len(end_states_line)):
            if index == len(end_states_line) - 1:
                self.end_states.append(end_states_line[index].split('\n')[0])
            else:
                self.end_states.append(end_states_line[index])

        start_states_line = lines[3].split(" ")
        for index in range(len(start_states_line)):
            if index == len(start_states_line) - 1:
                self.start_states.append(start_states_line[index].split('\n')[0])
            else:
                self.start_states.append(start_states_line[index])

        for index in range(4, len(lines)):
            transition_func_line = lines[index].split(" ")
            
            starting_state = str(transition_func_line[0])
            transition_symbol = transition_func_line[1]
            ending_state = str(transition_func_line[2]).split('\n')[0]

            transition_function = (starting_state, transition_symbol, ending_state);
            self.transition_functions.append(transition_function)        



class DFA:
    def __init__(self):
        self.num_states = 0
        self.states = []
        self.symbols = []
        self.end_states = []
        self.start_states = []
        self.transition_functions = []
    
    def convert_from_nfa(self, nfa):
        self.symbols = nfa.symbols
        start_dfa = nfa.start_states
        for state in start_dfa:
            for trans in nfa.transition_functions:
                if state == trans[0] and trans[1] == '$':
                    start_dfa.append(trans[2])
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
                for s in state_symbol:
                    for trans in nfa.transition_functions:
                        if s == trans[0] and trans[1] == '$':
                            state_symbol.append(trans[2])
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
                    if s == s1:
                        self.end_states.append(state)
                        break

        for state in self.states:
            for s1 in nfa.start_states:
                for s in state:
                    if s == s1:
                        self.start_states.append(state)
                        break


    def print_dfa(self):
        print('节点数量：',self.num_states)
        print('节点',self.states)
        print('路径',self.symbols)
        print('终止状态',self.end_states)
        print('起始状态',self.start_states)
        print('转化路径',self.transition_functions)