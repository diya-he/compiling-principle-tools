import json


def init_analysis_table():
    action = {
        '0': {
            'a': 'B',
            'b': 'D'
        },
        '1': {
            '#': 'acc'
        },
        '2': {
            'a': '4'
        },
        '3': {
            'b': '5'
        },
        '4': {
            'b': 'B'
        },
        '5': {
            'a': 'D'
        },
        '6': {
            'b': '8'
        },
        '7': {
            'a': '9'
        },
        '8': {
            '#': 'ABaBb'
        },
        '9': {
            '#': 'ADbDa'
        }
    }
    goto = {
        '0': {
            'A': '1',
            'B': '2',
            'D': '3'
        },
        '4': {
            'B': '6'
        },
        '5': {
            'D': '7'
        },
    }
    return action, goto


def message(status, message):
    if status == 'success':
        print(message + '\n')
    elif status == 'error':
        print(message + '\n')
    exit(0)


def analysis(status_stack, sym_stack, input_stack, *args):
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
        input_stack.pop()
    elif record == 'acc':
        return 'acc'
    else:
        lens = len(record) - 1
        for i in range(lens):
            if sym_stack.pop() == record[lens - i]:
                status_stack.pop()
            else:
                message('error', 'syntax error')
        sym_stack.append(record[0])
        status_stack.append(goto[status_stack[-1]][sym_stack[-1]])
    return 'continue'

if __name__ == '__main__':
    input_string = 'bccccccd#'
    input_stack = []
    for s in reversed(input_string):
        input_stack.append(s)

    if input_stack[0] != '#':
        message('error', 'ERROR: expect #')

    sym_stack = []
    sym_stack.append('#')

    status_stack = []
    status_stack.append('0')

    json_table = json.load(open('./Table/LR0_2.json', 'r', encoding="utf-8"))
    action = json_table['action']
    goto = json_table['goto']
    res = ''
    while not res == 'acc':
        print('状态栈:', status_stack)
        print('符号栈:', sym_stack)
        print('输入栈:', input_stack)
        print('-------------------')
        res = analysis(status_stack, sym_stack, input_stack, action, goto)

    message('success', 'analysis success')

