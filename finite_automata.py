import copy
import json

class NFA:
    def __init__(self):
        self.num_states = 0
        self.states = []
        self.symbols = []
        self.end_states = []
        self.start_states = []
        self.transition_functions = []

    def e_closure(self, state_table):
        for state in state_table:
            for trans in self.transition_functions:
                if state == trans[0] and trans[1] == '$':
                    state_table.append(trans[2])
        return state_table

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

class minimalDFA:
    def __init__(self):
        self.num_states = 0
        self.states = []
        self.symbols = []
        self.end_states = []
        self.start_states = []
        self.transition_functions = []

    def __mapping_array(self, mapping_dict, states_list, sym):
        for states_key in states_list:
            if len(states_key) == 1:
                continue
            for states_value in states_list:
                if len(states_key) == 1:
                    continue
                template_list = []
                # 从key中取数映射到value
                for key in states_key:
                    # print(key)
                    if (mapping_dict[sym][key] in states_value):
                        template_list.append(key)
                        states_key.remove(key)
                if states_key==[]:
                    states_list.remove(states_key)
                if template_list != []:
                    states_list.append(template_list)


    def minimize_from_dfa(self, dfa):
        self.symbols = dfa.symbols

        list_a = dfa.end_states
        list_b = []
        for i in dfa.states:
            if i not in list_a:
                list_b.append(i)
        # print(list_a)
        # print(list_b)
        status_list = []
        status_list.append(list_a)
        status_list.append(list_b)
        #映射路径到字典
        mapping_path = {}
        for sym in dfa.symbols:
            mapping_path[sym] = {}
            for i in range(dfa.num_states):
                mapping_path[sym][str(i)] = 'null'
        for sym in dfa.symbols:
            for tran in dfa.transition_functions:
                if tran[1] == sym:
                    mapping_path[sym][tran[0]] = tran[2]

        # for sym in dfa.symbols:
        #     for status in status_list:
        #         new_cl = []
        #         for i in status:
        #             if mapping_path[sym][i] not in status:
        #                 # print(mapping_path[sym][i])
        #                 if( len(status) > 1 ):
        #                     new_cl.append(i)
        #                     status.remove(i)
        #         if len(new_cl) and len(status):
        #             status_list.append(new_cl)
        while 1:
            status_list_bac = copy.deepcopy(status_list)
            for symbol in self.symbols:
                self.__mapping_array(mapping_path, status_list, symbol)
            for symbol in reversed(self.symbols):
                self.__mapping_array(mapping_path, status_list, symbol)
            if status_list_bac == status_list:
                break

        # print(status_list)
        self.num_states = len(status_list)
        self.states = status_list

        for status in status_list:
            for d in dfa.start_states:
                if d in status and status not in self.start_states:
                    self.start_states.append(status)
        for status in status_list:
            for d in dfa.end_states:
                if d in status and status not in self.end_states:
                    self.end_states.append(status)
        for status1 in status_list:
            for status2 in status_list:
                for sym in self.symbols:
                    if mapping_path[sym][status1[0]] in status2:
                        self.transition_functions.append((status1, sym, status2))
                        break

