import copy


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
        # 求初始节点的空闭包
        start_dfa = nfa.e_closure(start_dfa)
        self.states.append(start_dfa)
        for state in self.states:  # 状态
            for symbol in self.symbols:  # 路径标志
                state_symbol = []
                # 当前路径的下个新状态
                for s in state:
                    for trans in nfa.transition_functions:
                        if s == trans[0] and symbol == trans[1]:
                            state_symbol.append(trans[2])
                # 求空闭包
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


    def __function(self, S0s, cin):  # 获得S0状态下输入cin的所有输出，closure=__function(S0,'ε')
        result = []
        for S0 in S0s:
            for f in self.transition_functions:
                if f[0] == S0 and f[1] == cin:
                    return f[2]
        return None
    def __get_cls_n(self, S0s, ele):
        for i in S0s:
            if ele in i:
                return S0s.index(i)

    def __equ(self, l1, l2):
        for i in l1:
            flag = 1
            for j in l2:
                if set(i)==set(j):
                    flag = 0
            if flag==1:
                return False
        return True

    def minilization(self, S0s): # S0s为初态和终态集合的列表，[（1，2，3），（4，5）]
        result = copy.deepcopy(S0s)
        mappings = []
        while True:
            mappings.clear()
            for Cls in S0s:
                array = []       # array记录每个元素过某个输入后得到的元素
                mapping = dict()  # mapping映射字典，键值为array中的元素，值为S0中的原始元素集合
                for ele in Cls:
                    array.append([self.__get_cls_n(S0s, self.__function(ele, cin)) for cin in self.symbols])
                for i in range(len(array)):
                    if str(array[i]) in mapping:
                        mapping[str(array[i])].append(Cls[i])
                    else:
                        mapping[str(array[i])] = [Cls[i]]
                for key in mapping:
                    mappings.append(mapping[key])
            Cls = mappings
            if self.__equ(mappings, Cls):
                break

        self.states = mappings
        self.num_states = len(mappings)
        tmp_list = []
        for state in self.end_states:
            for map in mappings:
                if state in map and map not in tmp_list:
                    tmp_list.append(map)
                    break
        self.end_states = tmp_list

        tmp_list = []
        for state in self.start_states:
            for map in mappings:
                if state in map and map not in tmp_list:
                    tmp_list.append(map)
                    break
        self.start_states = tmp_list

        tmp_transition = []
        for transition in self.transition_functions:
            first = []
            third = []
            for map in mappings:
                if transition[0] in map:
                    first = map
                if transition[2] in map:
                    third = map
            if (first, transition[1], third) not in tmp_transition:
                tmp_transition.append((first, transition[1], third))
        self.transition_functions = tmp_transition
