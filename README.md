> Note: Most of the required data for this project is converted and stored using JSON, and a small portion has not been written yet, so it is directly placed in the initialization of the class. The solution is simple: write a function initialization class that reads JSON and implements data migration to JSON. JSON files are simple and easy to understand, so we will not elaborate on their respective meanings here.
* Project unresolved issues
  * LL1 recursive descent and table driver are not written using JSON reading, so the JSON files generated in the LL1 grammar code cannot be executed in the table driver and recursive descent code (although the JSON file code generated by the LL1 grammar has not been written yet)
  * The syntax of LR analysis with semantic stack is too absolute, and it is written in a specific grammar, which is not universal. I hope it can be improved
  * Minimizing DFA code has some bugs, some grammar execution results are incorrect, to be resolved

# Project Structure
`/data/`The folder contains NFA, DFA, and JSON files that minimize DFA

`/LL1analysis/`The folder contains four codes: top-down semantic computation based on L-translation mode, LL1 grammar judgment, recursive descent to solve LL1 grammar analysis, and table driven method to solve LL1 grammar analysis

`/LR0analysis/` 1、`/Table/`The folder stores the constructed LR0 analysis table;2、`/Grammer/`The folder stores grammar JSON files. The other codes in the folder are building LR0 analysis table code, LR0 main control program, and LR analysis with semantic stack

`/test/`The folder contains test files for minimizing DFA and NFA to DFA conversion

`FAtools.py`Encapsulating some tool classes of automata for easy use and reducing code redundancy, specific usage can be found in`/test/`saw inside that in the later stage of project development, we are considering writing a pages document to provide calls

`finite_automata`There are two categories inside, namely DFA and NFA


