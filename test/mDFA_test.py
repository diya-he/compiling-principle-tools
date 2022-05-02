from finite_automata import DFA,minimalDFA
import FAtools as fat
dfa = DFA()
minimalDFA = minimalDFA()

fat.construct_from_file(dfa, '../data/dfa.json')
minimalDFA.minimize_from_dfa(dfa)

fat.print_fa(minimalDFA)

fat.simple_state_fa(minimalDFA)
fat.print_fa(minimalDFA)
fat.save_fa_to_json(minimalDFA, '../data/minimal_dfa.json')

