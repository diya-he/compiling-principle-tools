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

`finite_automata.py`封装了两个类，一个是NFA，一个是DFA，本代码使用状态表法进行转化，时间复杂度初步计算为`O(n^3)`希望有大佬进行改进qwq

>代码流程在mian文件里，应该不难理解
```python
from finite_automata import NFA, DFA
import sys
filename = input('Enter the name of the NFA file: ')

if sys.version_info >= (3, 0):
    filename = input('Enter the name of the NFA file: ')
elif sys.version_info >= (2, 0):
    filename = raw_input('Enter the name of the NFA file: ')
else:
    print("Please update python to version 2.0 or newer")
    quit()

file = open(filename, 'r')
lines = file.readlines()
file.close()

nfa = NFA()
dfa = DFA()

nfa.construct_nfa_from_file(lines)

dfa.convert_from_nfa(nfa)

dfa.print_dfa()


```