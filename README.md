实现非常简单
txt文件解析如下:
```angular2html
2 NFA节点数量
ab NFA路径
1 NFA结束节点
0 NFA开始节点
0 a 0 NFA转化路径，以下都是
0 a 1   
0 b 1
1 b 1
```

`finite_automata.py`封装了两个类，一个是NFA，一个是DFA，本代码使用状态表法进行转化，时间复杂度初步计算为`O(n^4)`希望有大佬进行改进qwq

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