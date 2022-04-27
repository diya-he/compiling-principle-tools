from finite_automata import NFA, DFA

filename = input('Enter the name of the NFA file: ')

file = open(filename, 'r')
lines = file.readlines()
file.close()

nfa = NFA()
dfa = DFA()

nfa.construct_nfa_from_file(lines)

dfa.convert_from_nfa(nfa)

dfa.print_dfa()
