实现非常简单
`json`文件解析如下:
```json
{
  "num_states":2,
  "symbols": ["a","b"],
  "end_states": ["1"],
  "start_states": ["0"],
  "transition_functions": [
    ["0", "a", "0"],
    ["0", "a", "1"],
    ["0", "b", "1"],
    ["1", "b", "1"]
  ]
}
```

`finite_automata.py`封装了几个类，本代码使用造表法进行转化，时间复杂度初步计算为`O(n^3)`
等项目写完后预计会写一份使用文档

```python
#NFA to DFA test
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
```
```python
#minimize DFA test
from finite_automata import DFA,minimalDFA
import FAtools as fat
dfa = DFA()
minimalDFA = minimalDFA()

fat.construct_from_file(dfa, '../data/dfa.json')
minimalDFA.minimize_from_dfa(dfa)

fat.print_fa(minimalDFA)

fat.simple_state_fa(minimalDFA)
# fat.print_fa(minimalDFA)
fat.save_fa_to_json(minimalDFA, '../data/minimal_dfa.json')
```
