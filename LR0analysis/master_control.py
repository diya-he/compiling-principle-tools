def init_analysis_table():
    action = {
        0:{
            'a':'$',
            'b':'$'
        },
        1:{
            '#':'acc'
        },
        2:{
            'a':4
        },
        3:{
            'b':5
        },
        4:{
            'b':'$'
        },
        5:{
            'a':'$'
        },
        6:{
            'b':8
        },
        7:{
            'a':9
        },
        8:{
            '#':'BaBb'
        },
        9:{
            '#':'DbDa'
        }
    }
    goto = {
        0:{
            'A':1,
            'B':2,
            'D':3
        },
        4:{
            'B':6
        },
        5:{
            'D':7
        },
    }
    return action, goto

def analysis(status_stack, sym_stack, input_stack, *args):
    status = status_stack[-1]
    sym_stack = sym_stack[-1]
    input_stack = input_stack[-1]
    

if __name__ == '__main__':
    input_string = 'ab#'
    input_stack = []
    for s in reversed(input_string):
        input_stack.append(s)

    if input_stack[0] != '#':
        message('error', 'ERROR: expect #')
    
    sym_stack = []
    sym_stack.append('#')

    status_stack = []
    status_stack.append(0)

    action, goto = init_analysis_table()

    analysis(status_stack, sym_stack, input_stack, action, goto)
    
    
    

    