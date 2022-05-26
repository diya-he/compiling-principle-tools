import json


def message(status, message):
    if status == 'success':
        print(message + '\n')
    elif status == 'error':
        print(message + '\n')
    exit(0)


class Value:
    def __init__(self, val, scope):
        self.val = val
        self.s = scope


def semantic_action(record, analysis_stack):
    if record[0] == 'N':
        print(analysis_stack[-1].val)
    elif record[0] == 'S':
        if len(record) - 1 > 0:
            analysis_stack[-3].val = analysis_stack[-3].val + analysis_stack[-1].val
            analysis_stack.pop()
            analysis_stack.pop()
        else:
            analysis_stack.append(Value(0, None))
    elif record[0] == 'B':
        if record[1] == '0':
            analysis_stack[-1] = Value(None, None)
            analysis_stack[-1].val = 0
        elif record[1] == '1':
            analysis_stack[-1] = Value(None, None)
            print(analysis_stack[-2].s)
            analysis_stack[-1].val = pow(2, -analysis_stack[-2].s)
    elif record[0] == 'M':
        analysis_stack.append(Value(None, 1))
    elif record[0] == 'P':
        analysis_stack.append(Value(None, analysis_stack[-2].s + 1))


def analysis(status_stack, sym_stack, input_stack, analysis_stack, *args):
    status = status_stack[-1]
    string = input_stack[-1]
    record = ''
    try:
        record = action[status][string]
    except:
        message('error', 'syntax error')
    if record.isdigit():
        status_stack.append(record)
        sym_stack.append(string)
        analysis_stack.append('-')
        input_stack.pop()
    elif record == 'acc':
        semantic_action('N.MS', analysis_stack)
        return 'accept'
    else:
        lens = len(record) - 1
        for i in range(lens):
            if sym_stack.pop() == record[lens - i]: #lens要重新调整一下
                status_stack.pop()
            else:
                message('error', 'syntax error')
        sym_stack.append(record[0])
        semantic_action(record, analysis_stack)
        status_stack.append(goto[status_stack[-1]][sym_stack[-1]])
    return 'continue'


if __name__ == '__main__':
    input_string = '.10101#'
    input_stack = []
    for s in reversed(input_string):
        input_stack.append(s)

    if input_stack[0] != '#':
        message('error', 'ERROR: expect #')

    sym_stack = []
    sym_stack.append('#')

    status_stack = []
    status_stack.append('0')

    analysis_stack = []
    analysis_stack.append('-')

    json_table = json.load(open('./Table/semantic_stack_LR0.json', 'r', encoding="utf-8"))
    action = json_table['action']
    goto = json_table['goto']
    res = 'continue'
    while not res == 'accept':
        print('状态栈:', status_stack)
        print('符号栈:', sym_stack)
        print('输入栈:', input_stack)
        print('-------------------')
        res = analysis(status_stack, sym_stack, input_stack, analysis_stack, action, goto)

    message('success', 'analysis success')