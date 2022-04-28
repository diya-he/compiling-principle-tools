from finite_automata import NFA, DFA
import sys

# if sys.version_info >= (3, 0):
#     filename = input('Enter the name of the NFA file: ')
# elif sys.version_info >= (2, 0):
#     filename = raw_input('Enter the name of the NFA file: ')
# else:
#     print("Please update python to version 2.0 or newer")
#     quit()

file = open('nfa.json', 'r')
lines = file.readlines()
file.close()

nfa = NFA()
dfa = DFA()

nfa.construct_nfa_from_file(lines)
# nfa.print_nfa()
dfa.convert_from_nfa(nfa)
dfa.save_dfa_json()
dfa.print_dfa()
