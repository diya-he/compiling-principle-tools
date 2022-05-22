from finite_automata import DFA
import FAtools as fat
dfa = DFA()

fat.construct_from_file(dfa, '../data/dfa2.json')
fat.print_fa(dfa)
print('--------------------------------')
S0s = [dfa.end_states, list(set(dfa.states).difference(set(dfa.end_states)))]
dfa.minilization(S0s)
# fat.simple_state_fa(dfa)
fat.print_fa(dfa)
#dfa.convert_from_nfa(dfa)
# fat.save_fa_to_json(dfa, '../data/minimal_dfa.json')