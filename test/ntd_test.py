from finite_automata import NFA, DFA
import FAtools as fat
nfa = NFA()
dfa = DFA()

filepath = '../data/nfa.json'
fat.construct_from_file(nfa, filepath)
# fat.print_fa(nfa)

dfa.convert_from_nfa(nfa)
filepath = "../data/dfa.json"
fat.simple_state_fa(dfa)
fat.save_fa_to_json(dfa, filepath)
fat.print_fa(dfa)
