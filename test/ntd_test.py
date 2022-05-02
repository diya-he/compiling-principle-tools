from finite_automata import NFA, DFA
import sys

# if sys.version_info >= (3, 0):
#     filename = input('Enter the name of the NFA file: ')
# elif sys.version_info >= (2, 0):
#     filename = raw_input('Enter the name of the NFA file: ')
# else:
#     print("Please update python to version 2.0 or newer")
#     quit()

file = open('../data/nfa.json', 'r')
lines = file.readlines()
file.close()

nfa = NFA()
dfa = DFA()

filepath = '../data/nfa.json'
nfa.construct_nfa_from_file(lines, filepath)
nfa.print_nfa()
dfa.convert_from_nfa(nfa)
filepath = "../data/dfa.json"
dfa.save_dfa_json(filepath)
dfa.print_dfa()
