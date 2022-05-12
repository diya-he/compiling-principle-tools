# S->Aa|b
# A->SB
# B->ab

#       a       b       #
# S           S->bA
# A  A->abaA          A->$


# 步骤     分析栈     剩余输入串       推导所用产生式或匹配
# 1       #S       babaaba#         S->bA
# 2       #Ab      babaaba#         b匹配

def message(status, message):
    if status == 'success':
        print(message + '\n')
    elif status == 'error':
        print(message + '\n')
    exit(0)


def S(analysis_stack):
    analysis_stack.pop()
    analysis_stack.append('A')
    analysis_stack.append('b')


def A(analysis_stack, str):
    if str == 'a':
        analysis_stack.pop()
        analysis_stack.append('A')
        analysis_stack.append('a')
        analysis_stack.append('b')
        analysis_stack.append('a')
    elif str == '#':
        analysis_stack.pop()
        return
    else:
        message('error', 'syntax error')


def analysis(analysis_stack, str_stack):
    analysis = analysis_stack[-1]
    if analysis == 'S':
        S(analysis_stack)
    elif analysis == 'A':
        str = str_stack[-1]
        A(analysis_stack, str)
    else:
        str = str_stack[-1]
        if str == analysis:
            analysis_stack.pop()
            str_stack.pop()
        else:
            message('error', 'syntax error')


if __name__ == '__main__':
    input_string = 'babaabaabaabaabaabaabaabaaba#'
    str_stack = []
    for s in reversed(input_string):
        str_stack.append(s)

    if str_stack[0] != '#':
        message('error', 'ERROR: expect #')

    analysis_stack = ['#']
    analysis_stack.append('S')

    while len(analysis_stack) and len(str_stack):
        print('分析栈: ' + str(analysis_stack))
        print('剩余输入串: ' + str(str_stack))
        analysis(analysis_stack, str_stack)

    if not (len(analysis_stack) and len(str_stack)):
        message('success', '分析成功')
